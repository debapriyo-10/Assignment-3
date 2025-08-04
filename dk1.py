class Solution:
    def insertInMiddle(self, head, x):
        #code here
        new=Node(x)
        if head is  None:
            return new
        if head.next is None:
            head.next=new
            return head
            
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        new.next = slow.next
        slow.next = new
        
        return head 