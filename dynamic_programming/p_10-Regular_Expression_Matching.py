def isMatching(v, p):
    if p == ".":
        return True
    return v == p


def dealing_with_dot(state_obj):
    if "mapping" in state_obj:
        if "." in state_obj["mapping"]:
            for p in state_obj["mapping"]:
                state_obj["mapping"][p] += state_obj["mapping"]["."]
                state_obj["mapping"][p] = list(set(state_obj["mapping"][p]))


def get_union_mapping(nfa_states, state_ids):
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
            print("[Char `{}`][In state{}]".format(c, cur_state["name"]))
            for p in cur_state["mapping"].keys():
                print("\t`{}`:{}".format(p, cur_state["mapping"][p]))
            print("\t-------")
            for p in cur_state["mapping"].keys():
                if isMatching(c, p):
                    next_state_id = cur_state["mapping"][p][0]
                    print("\t`{}` matching `{}` : go to state {}".format(c, p, next_state_id))
                    break

            if next_state_id is None:
                return False
            cur_state = self.states_obj[next_state_id]
        print("All string went through", cur_state["is_final"])
        if cur_state["is_final"]:
            return True
        else:
            return False


def convert_NFA_to_DFA(NFA_states, state_ctr):
    print("NFA_states", NFA_states)
    NFA_states_ = dict(NFA_states)
    state_itr = 0
    mapping_state_map = dict()
    while state_itr < state_ctr:
        state_id = "s_" + str(state_itr)
        state = NFA_states_[state_id]
        print(state['name'], state)
        state_itr += 1

        if not "mapping" in state:
            continue

        for pattern in state["mapping"].keys():
            # key can go to states `states_to_go`
            states_to_go = state["mapping"][pattern]
            # no need to create new state
            if len(states_to_go) == 1:
                continue
            else:
                # is final and the new_mapping for the new state
                mapping_state_id = "-".join(sorted(states_to_go))
                if mapping_state_id not in mapping_state_map:
                    new_is_final, new_mappings = get_union_mapping(NFA_states_, states_to_go)
                    new_state_id = "s_" + str(state_ctr)
                    print("Create new state for", pattern, states_to_go, "as", new_state_id)
                    state_ctr += 1
                    state["mapping"][pattern] = [new_state_id]
                    NFA_states_[new_state_id] = {
                        "name": new_state_id,
                        "is_final": new_is_final,
                        "mapping": new_mappings
                    }
                    mapping_state_map[mapping_state_id] = new_state_id
                print("Converting {} to {}".format(states_to_go, [mapping_state_map[mapping_state_id]]))
                NFA_states_[state_id]["mapping"][pattern] = [mapping_state_map[mapping_state_id]]

    print(NFA_states_)
    print("==================")
    return NFA_states_


def str_to_epsilonNFA(str_):
    state_id = ""
    next_state_id = ""

    state_ctr = 0
    nfa_states = {}

    for i, c in enumerate(str_):
        if c == "*":
            # `@` for `epsilon transition`
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
                del mapping["@"]
    # delete "@" and deal with "." (any state . can go others can go)
    for state_id in NFA_states.keys():
        state = NFA_states[state_id]
        if "mapping" in state:
            mapping = state["mapping"]
            if "." in mapping:
                for k in list(mapping.keys()):
                    if k == ".":
                        continue
                    mapping[k] = list(set(mapping[k] + mapping["."]))
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


def main():
    epsilonNFA_states, state_ctr = str_to_epsilonNFA("a.*b")
    print("epsilonNFA_states")
    print(epsilonNFA_states)
    NFA_states = epsilonNFA_to_NFA(epsilonNFA_states)
    print("NFA_states")
    print(NFA_states)
    dfa_states = convert_NFA_to_DFA(NFA_states, state_ctr)
    machine = DFA(dfa_states)
    print("dfa_states")
    print(dfa_states)
    print(machine.isAcceptable("acccccb"))


if __name__ == '__main__':
    main()
    exit()
    sol = Solution()
    s = "mississippi"
    p = "mis*is*ip*."
    print(sol.isMatch(s, p))
