import typing
from typing import Optional
class ListNode:
    def __init__(self,next=None,val=0):
        self.next=next
        self.val=val
class MyLinkedList:

    def __init__(self):
        self.dummy_head=ListNode()
        self.size=0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        count=0
        current=self.dummy_head.next
        while(count<index):
            current=current.next
            count=count+1
        return current.val

    def addAtHead(self, val: int) -> None:
        newhead=ListNode(self.dummy_head.next,val)
        self.dummy_head.next=newhead
        self.size+=1

    def addAtTail(self, val: int) -> None:
        current=self.dummy_head
        while(current.next!=None):
            current=current.next
        current.next=ListNode(None,val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        count = 0
        current = self.dummy_head
        while (count < index):
            current = current.next
            count = count + 1
        IndexNode=current
        NewNode=ListNode(IndexNode.next,val)
        IndexNode.next=NewNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return
        count = 0
        current = self.dummy_head
        while (count < index):
            current = current.next
            count = count + 1
        frontNode=current
        frontNode.next=frontNode.next.next
        self.size-=1