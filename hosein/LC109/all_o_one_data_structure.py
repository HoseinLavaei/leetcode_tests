class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_map = {}
        self.head = Node(0)
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _insert_before(self, node, new_node):
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node

    def inc(self, key: str) -> None:
        if key not in self.key_map:
            if self.head.next.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
            else:
                new_node = self.head.next
            new_node.keys.add(key)
            self.key_map[key] = new_node
        else:
            node = self.key_map[key]
            node.keys.remove(key)
            next_node = node.next
            if next_node.count != node.count + 1:
                new_node = Node(node.count + 1)
                self._insert_after(node, new_node)
            else:
                new_node = next_node
            new_node.keys.add(key)
            self.key_map[key] = new_node
            if not node.keys:
                self._remove_node(node)

    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return
        node = self.key_map[key]
        node.keys.remove(key)
        if node.count == 1:
            del self.key_map[key]
        else:
            prev_node = node.prev
            if prev_node.count != node.count - 1:
                new_node = Node(node.count - 1)
                self._insert_before(node, new_node)
            else:
                new_node = prev_node
            new_node.keys.add(key)
            self.key_map[key] = new_node
        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""