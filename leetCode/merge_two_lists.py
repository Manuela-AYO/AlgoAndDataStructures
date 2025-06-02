# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = ListNode()
        current_node = final_list
        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            current_node = current_node.next
        if list1:
            current_node.next = list1
        elif list2:
            current_node.next = list2
        return final_list.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and list2:
            final_list = ListNode(min(list1.val, list2.val))
            current_node = final_list
            if list1.val <= list2.val:
                list1 = list1.next
            else:
                list2 = list2.next
        else:
           return list1 if list1 else list2
        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            current_node = current_node.next
        if list1:
            current_node.next = list1
        elif list2:
            current_node.next = list2
        return final_list