from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        res = ""
        curr = self
        while curr is not None:
            res += f'{curr.val} -> '
            curr = curr.next

        print(res)


class Solution:
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recur(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if l1 is None and l2 is None and carry == 0:
                return None

            next1 = next2 = None
            sum = carry
            if l1 is not None:
                sum += l1.val
                next1 = l1.next
            if l2 is not None:
                sum += l2.val
                next2 = l2.next

            return ListNode(sum % 10, recur(next1, next2, sum // 10))

        return recur(l1, l2, 0)

    def solve_iter(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        curr = result
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1+val2+carry, 10)
            curr.next = ListNode(out)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


Solution().solve(ListNode(2, ListNode(4, ListNode(3, None))),
                 ListNode(5, ListNode(6, ListNode(4, None)))).print()

Solution().solve_iter(ListNode(2, ListNode(4, ListNode(3, None))),
                      ListNode(5, ListNode(6, ListNode(4, None)))).print()
