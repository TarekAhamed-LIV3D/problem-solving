class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

linked_list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

result_head = deleteDuplicates(linked_list)

while result_head:
    print(result_head.val, end=" ")
    result_head = result_head.next