class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

#list1=[1,2,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
#list2=[1,3,4]
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next