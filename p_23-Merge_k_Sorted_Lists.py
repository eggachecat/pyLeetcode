import random
from data_structures.heap import Heap as saHeap
from data_structures.queue import Queue as saQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_node_list(head):
    vals = []
    while head is not None:
        vals.append(head.val)
        head = head.next
    print(vals)


class Solution:
    def connect_node(self, tail, num):
        tail.next = num
        tail = tail.next
        num = num.next
        return num, tail

    def merge_two_list(self, nums1, nums2):

        num1 = nums1
        num2 = nums2

        if num1.val < num2.val:
            num_head = num_tail = ListNode(num1.val)
            num1 = num1.next
        else:
            num_head = num_tail = ListNode(num2.val)
            num2 = num2.next
        while True:

            if num1 is None:
                while num2 is not None:
                    num2, num_tail = self.connect_node(num_tail, num2)
                break

            if num2 is None:
                while num1 is not None:
                    num1, num_tail = self.connect_node(num_tail, num1)
                break

            if num1.val < num2.val:
                num1, num_tail = self.connect_node(num_tail, num1)
            else:
                num2, num_tail = self.connect_node(num_tail, num2)

        return num_head

    def mergeKLists(self, lists):

        lists = list(filter(lambda x: x is not None, lists))

        if lists == []:
            return lists

        while True:
            n_lists = len(lists)
            if n_lists == 1:
                return lists[0]

            new_lists = []
            pairs = [[i, i + 1] if i + 1 < n_lists else (i,) for i in range(0, n_lists, 2)]

            for pair in pairs:
                if len(pair) == 2:
                    new_lists.append(self.merge_two_list(lists[pair[0]], lists[pair[1]]))
                else:
                    new_lists.append(lists[pair[0]])

            lists = new_lists


def gen_rand_num():
    num = random.randint(0, 1000)
    # print(num)
    return num


class SolutionWithHeap:
    def mergeKLists(self, lists):
        heap = saHeap()
        n_lists = len(lists)
        ptrs = [lists[i] for i in range(n_lists)]
        valMap = dict()

        sol = None
        head = None

        for i in range(n_lists):
            ptr = ptrs[i]
            val = ptr.val
            heap.append(val)
            ptrs[i] = ptr.next
            if val not in valMap:
                valMap[val] = saQueue()
            valMap[val].enter(ptr.next)

        heap.build_min_heap()

        while True:
            heap.min_heapify(0)
            minVal = heap.array[0]
            print("min_heapify", minVal, heap.array, heap.max_index)
            if sol is None:
                head = sol = ListNode(minVal)
            else:
                sol.next = ListNode(minVal)
                sol = sol.next
            ptr = valMap[minVal].delete()  # ptrs[valMap[minVal]]
            if ptr is not None:
                newVal = ptr.val
                heap.array[0] = newVal
                if newVal not in valMap:
                    valMap[newVal] = saQueue()
                valMap[newVal].enter(ptr.next)
            else:
                heap.swap(0, heap.max_index)
                heap.max_index -= 1

            if heap.max_index < 0:
                break
        return head


if __name__ == '__main__':
    # s = Solution()
    s = SolutionWithHeap()

    k = 3
    nums_lists = []
    N = 3

    raw_nums_lists = [[gen_rand_num() for __ in range(N)] for _ in range(k)]
    for r in raw_nums_lists:
        r.sort()
    raw_nums_lists = [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
    for _ in range(len(raw_nums_lists)):
        print("========================")
        num_ = num_head_ = ListNode(raw_nums_lists[_][0])
        for __ in range(1, len(raw_nums_lists[_])):
            num_.next = ListNode(raw_nums_lists[_][__])
            num_ = num_.next
        nums_lists.append(num_head_)

    for ptr in nums_lists:
        print_node_list(ptr)
    print("========================")
    test = s.mergeKLists(nums_lists)
    print("++++++++++++++++++++++++++++++++")
    print_node_list(test)
