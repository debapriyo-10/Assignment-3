# Question 1 : Linked List Insertion 
class Node:
	def __init__(self, data):   
		self.data = data
		self.next = None
class Solution : 
    def insertAtEnd(self,head,x):
        new=Node(x)
        if head == None:
             return new
        current=head
        while current.next:
             current=current.next
        current.next=new
        return head     



# Question 2 : Insertion at middle of LInked List 
class Node:
	def __init__(self, data):   
		self.data = data
		self.next = None
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
    


# Question 3 : Delete a node
class Node:
	def __init__(self, data):   
		self.data = data
		self.next = None    

def deleteNode(head,x):
      if x==1:
            return head.next
      current=head
      for _ in range (x-2):           
            current=current.next
      if current.next:
            current.next=current.next.next
      return head      

            
