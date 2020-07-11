# LeetCode - Middle of a Linked List (Two Pointers)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # solution 1 works
        #first = ListNode(val = head.val, next = head.next)
        #second = ListNode(val = head.val, next = head.next)
        
        # solution 2 works
        first = head
        second = head
        while(second != None):
            second = second.next
            if(second == None): return first
            first = first.next
            second = second.next
        
        return first
        
#https://www.youtube.com/watch?v=wq4OZZ3YLj4
