# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        tail_ = last = head_ = head

        i = 0
        while i < k:
            tail_ = tail_.next
            i += 1
        print("head_")
        printListNode(head_)

        print("tail_")
        printListNode(tail_)

        last = head_
        tmp = head_.next
        head_.next = last
        head_ = tmp


        print("head_")
        printListNode(head_)
        print("tmp")
        printListNode(tmp)
        print("tail_")
        printListNode(tail_)


def printListNode(head_):
    to_be_printed = []
    while head_ is not None:
        to_be_printed.append(head_.val)
        head_ = head_.next
    print(to_be_printed)


if __name__ == '__main__':
    s = Solution()

    head = ptr = ListNode(0)
    for i in range(1, 10):
        ptr.next = ListNode(i)
        ptr = ptr.next
    printListNode(head)

    s.reverseKGroup(head, 3)
