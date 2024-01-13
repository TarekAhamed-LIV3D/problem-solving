class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA

listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)
listA.next.next.next.next = ListNode(5)

listB = ListNode(5)
listB.next = ListNode(0)
listB.next.next = ListNode(1)
listB.next.next.next = listA.next.next

solution = Solution()
result = solution.getIntersectionNode(listA, listB)

if result:
    print("Intersection node value:", result.val)
else:
    print("No intersection")
