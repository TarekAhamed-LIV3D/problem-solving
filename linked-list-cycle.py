class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        tortoise = head
        hare = head.next

        while tortoise != hare:
            if not hare or not hare.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

solution = Solution()
result = solution.hasCycle(head)

print("Does the linked list have a cycle?", result)