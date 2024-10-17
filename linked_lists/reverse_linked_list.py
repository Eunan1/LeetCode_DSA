class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def reverseList(head):

    prev = None
    curr = head

    while curr:

        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        

        

