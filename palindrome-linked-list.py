class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_second_half = reverse_list(slow)

        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next

        return True

linked_list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
solution = Solution()
result = solution.isPalindrome(linked_list)

print("Is palindrome:", result)
