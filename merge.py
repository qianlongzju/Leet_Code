class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1, head2):
    dummy = Node(0)
    head = dummy
    while head1 and head2:
        if head1.data < head2.data:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    if head1:
        head.next = head1
    if head2:
        head.next = head2
    return dummy.next

def getHead(start, end):
    """helper function for constructing a list of Nodes"""
    nodes = []
    for i in range(start, end):
        nodes.append(Node(i))
        if len(nodes) >= 2:
            nodes[-2].next = nodes[-1]
    if not nodes:
        return None
    return nodes[0]

def printNodes(head):
    """print the list of Nodes"""
    if not head:
        return
    print head.data,
    head = head.next
    while head:
        print "->", head.data,
        head = head.next
    print '*' * 50

if __name__ == '__main__':
    head1 = getHead(1, 15)
    head2 = getHead(11, 20)

    head = merge(head1, head2)

    printNodes(head1)
    printNodes(head2)
    printNodes(head)


