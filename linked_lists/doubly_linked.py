class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def add_node(node, node_to_add):

    # prevNode |-------------------->| node
    #          ----- node_to_add ----- 

    prevNode = node.prev

    node_to_add.next = node
    node_to_add.prev = prevNode
    node.prev = node_to_add
    prevNode.next = node_to_add
