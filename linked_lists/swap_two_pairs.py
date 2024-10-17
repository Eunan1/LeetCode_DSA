class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None



def swap_pairs(head):
    # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head

        dummy = head.next               # Step 5
        prev = None                     # Intialize for step 3
        while head and head.next:
            if prev:
                prev.next = head.next   
            prev = head                 # Set prev and head to same pos

            next_node = head.next.next  # position of next two nodes for swap
            head.next.next = head       # Remove link betweem grouped nodes
                                        # for swapping and swap link

            head.next = next_node       
            head = next_node            

        return dummy
    
    
    

    



# 1 -> 2 -> 3 -> 4 -> 5 -> 6


# 2 -> 1 -> 4 -> 3 -> 6 -> 5

#            ______________
#           |              |
#           |              |
# 1 <- 2    3 <- 4    5 <- 6
# |              |
# |______________|
#  