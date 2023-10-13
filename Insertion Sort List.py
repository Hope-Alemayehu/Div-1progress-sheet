# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        dummy=ListNode(0,head)
        prev,cur=head,head.next
        
        while cur:
            #f they are in order
            if cur.val>=prev.val:
                prev,cur=cur,cur.next
                continue
            #if that's not the case we need to start from the beginning
            tmp=dummy
            while cur.val>tmp.next.val:
                tmp=tmp.next

            prev.next=cur.next
            cur.next=tmp.next
            tmp.next=cur
            cur=prev.next
        return dummy.next


