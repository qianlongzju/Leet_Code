class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        i = -1
        while node:
            if i == index:
                break
            node = node.next
            i += 1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.size += 1
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.size += 1
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return -1
        if index == self.size:
            self.addAtTail(val)
            return
        self.size += 1
        node = self.head
        i = 0
        while node:
            if i == index:
                break
            node = node.next
            i += 1
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        node = self.head
        i = 0
        while node:
            if i == index:
                break
            node = node.next
            i += 1
        node.next = node.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
