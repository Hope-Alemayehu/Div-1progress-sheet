class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        node_to_delete = self.head.next
        self.head.next = node_to_delete.next
        node_to_delete.next.prev = self.head
        node_to_delete.next = None
        node_to_delete.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        node_to_delete = self.tail.prev
        self.tail.prev = node_to_delete.prev
        node_to_delete.prev.next = self.tail
        node_to_delete.next = None
        node_to_delete.prev = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
