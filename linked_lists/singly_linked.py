# Basic example of how to set up nodes

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)


# Travel through a liinked list
# Get the num of all numbers

def travelSum(head):
    ans = 0

    while head:
        ans += head.val
        head = head.next

    return ans


# Add a node to a linked list

def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Delete a node from the linked list.

# Nodes can only be accessed from previous node so we can kill connection
# as shown below.

def delete_node(prev_node):
    prev_node.next = prev_node.next.next
    # Only way to access next node was from previous node.
    # We delete that node by setting it equal to next.next