class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
    ## If the list is empty, new node becomes head,
        if self.head is None:
            self.head = new_node
            return
    ## Otherwise,
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        def _sum(node):
            if node is None:
                return 0
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        def _reverse(prev, current):
            if current is None:
                return prev
            nxt = current.next
            current.next = prev
            return _reverse(current, nxt)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        def _search(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search(node.next)

        return _search(self.head)

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")