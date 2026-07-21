# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val : 
                curr.next = list1 #this is connecting the nodes
                curr = list1 #this is moving curr to the lis1 node that was merged
                list1 = list1.next #moving list1 pointer ahead 
            else:
                curr.next = list2 #when list1 and list2 values are equal we are setting list2 as default
                curr = list2
                list2 = list2.next 
        
        curr.next = list1 if list1 else list2 #while loop will stop if any one list ends, so need to point to the remaning list 

        return d.next 
