def isMatching(v, p):
    if p == ".":
        return True

    if p[0] == "#":
        return not v == p[1:]
    else:
        return v == p


class DFA:
    def __init__(self, states_obj, start_id="s_0"):
        self.states_obj = states_obj
        self.start_id = start_id
        self.start_state = self.states_obj[self.start_id]

    def isAcceptable(self, str_):

        cur_state = self.start_state
        for c in str_:
            next_state_id = None
            if "mapping" not in cur_state:
                return False

            for p in cur_state["mapping"].keys():
                if isMatching(c, p):
                    print("in state", cur_state["name"])
                    next_state_id = cur_state["mapping"][p][0]
                    print(c, "matching..", p, "go to state", next_state_id)
                    break

            if next_state_id is None:
                return False
            cur_state = self.states_obj[next_state_id]

        if cur_state["is_final"]:
            return True
        else:
            return False


def get_union_result(nfa_states, state_ids):
    new_mappings = {}
    new_is_final = False
    for state_id in state_ids:
        state_ = nfa_states[state_id]

        if state_["is_final"]:
            new_is_final = True

        if "mapping" in state_:
            for key_, states_to_go_ in state_["mapping"].items():
                if key_ in new_mappings:
                    new_mappings[key_] = list(set(new_mappings[key_] + states_to_go_))
                else:
                    new_mappings[key_] = list(states_to_go_)

    return new_is_final, new_mappings


def convert_NFA_to_DFA(NFA_states, state_ctr):
    NFA_states_ = dict(NFA_states)
    state_itr = 0
    while state_itr < state_ctr:
        state_id = "s_" + str(state_itr)
        state = NFA_states_[state_id]
        if not "mapping" in state:
            state_itr += 1
            continue

        for key in state["mapping"].keys():
            states_to_go = state["mapping"][key]
            if len(states_to_go) == 1:
                state_itr += 1
                continue
            else:
                new_state_id = "s_" + str(state_ctr)
                state_ctr += 1
                state["mapping"][key] = [new_state_id]
                new_is_final, new_mappings = get_union_result(NFA_states_, states_to_go)
                NFA_states_[new_state_id] = {
                    "name": new_state_id,
                    "is_final": new_is_final,
                    "mapping": new_mappings
                }

    return NFA_states_


def str_to_epsilonNFA(str_):
    state_id = ""
    next_state_id = ""

    state_ctr = 0
    nfa_states = {}

    for i, c in enumerate(str_):
        if c == "*":
            nfa_states[state_id]["mapping"]["@"] = [state_id, next_state_id]
            nfa_states[state_id]["mapping"][str_[i - 1]] += [state_id]
        else:
            state_id = "s_" + str(state_ctr)
            next_state_id = "s_" + str(state_ctr + 1)
            state_ctr += 1
            nfa_states[state_id] = {
                "name": state_id,
                "is_final": False,
                "mapping": {
                    c: [next_state_id]
                }
            }
    nfa_states[next_state_id] = {
        "name": next_state_id,
        "is_final": True,
    }
    return nfa_states, state_ctr + 1


def deal_with_E_closure(epsilonNFA_states, state_id):
    isVisited = {}
    curr_state = epsilonNFA_states[state_id]

    while True:
        state_id_ = None
        for state_id__ in curr_state["mapping"]["@"]:
            if state_id__ not in isVisited:
                isVisited[state_id__] = True
                state_id_ = state_id__
                break

        if state_id_ is None:
            return

        state_ = epsilonNFA_states[state_id_]
        curr_state["is_final"] = curr_state["is_final"] or state_["is_final"]
        if "mapping" in state_:
            for input_ in state_["mapping"]:
                if input_ in curr_state["mapping"]:
                    curr_state["mapping"][input_] = list(set(curr_state["mapping"][input_] + state_["mapping"][input_]))
                else:
                    curr_state["mapping"][input_] = list(state_["mapping"][input_])


def epsilonNFA_to_NFA(epsilonNFA_states):
    NFA_states = dict(epsilonNFA_states)
    for state_id in NFA_states.keys():
        state = NFA_states[state_id]
        if "mapping" in state:
            mapping = state["mapping"]
            if "@" in mapping:
                deal_with_E_closure(NFA_states, state_id)

    # delete "@" and deal with "." (any state . can go others can go)
    for state_id in NFA_states.keys():
        state = NFA_states[state_id]
        if "mapping" in state:
            mapping = state["mapping"]
            if "@" in mapping:
                del mapping["@"]
            if "." in mapping and len(list(mapping.keys())) > 1:
                for k in list(mapping.keys()):
                    mapping["#" + k] = list(mapping["."])

                for k in list(mapping.keys()):
                    mapping[k] = list(set(mapping[k] + mapping["."]))

                print(mapping)

                del mapping["."]
                del mapping["#."]
                print("#.", mapping)

    return NFA_states


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        epsilonNFA_states, state_ctr = str_to_epsilonNFA(p)
        print(epsilonNFA_states)
        NFA_states = epsilonNFA_to_NFA(epsilonNFA_states)
        print(NFA_states)
        DFA_states = convert_NFA_to_DFA(NFA_states, state_ctr)
        print(DFA_states)
        machine = DFA(DFA_states)

        return machine.isAcceptable(s)


Z = {'s_0': {'name': 's_0', 'is_final': False, 'mapping': {'p': ['s_1', 's_0'], '@': ['s_0', 's_1']}},
     's_1': {'name': 's_1', 'is_final': False, 'mapping': {'.': ['s_2']}},
     's_2': {'name': 's_2', 'is_final': True}}

Z_ = {'s_0': {'name': 's_0', 'is_final': False, 'mapping': {'p': ['s_1', 's_0'], '@': ['s_0', 's_1']}},
      's_1': {'name': 's_1', 'is_final': False, 'mapping': {'.': ['s_2']}},
      's_2': {'name': 's_2', 'is_final': True}}

Z__ = {'s_0': {'name': 's_0', 'is_final': False, 'mapping': {'p': ['s_2', 's_1', 's_0'], '.': ['s_2']}},
       's_1': {'name': 's_1', 'is_final': False, 'mapping': {'.': ['s_2']}},
       's_2': {'name': 's_2', 'is_final': True}}


def main():
    epsilonNFA_states, state_ctr = str_to_epsilonNFA(".*b")
    NFA_states = epsilonNFA_to_NFA(epsilonNFA_states)
    print(NFA_states, state_ctr)
    dfa_states = convert_NFA_to_DFA(NFA_states, state_ctr)
    print(dfa_states)

    machine = DFA(dfa_states)
    print(machine.isAcceptable("aaaassdkfhkjfdbab"))
    # print(dfa_states)


if __name__ == '__main__':
    # main()

    sol = Solution()
    s = "mississippi"
    p = "mis*is*ip*."
    print(sol.isMatch(s, p))
