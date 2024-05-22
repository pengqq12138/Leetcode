import typing
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while(head.val==val):
            head=head.next
        phead=head
        while(phead.next!=None):
            if(phead.next.val==val):
                phead.next=phead.next.next
        head=phead

# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

