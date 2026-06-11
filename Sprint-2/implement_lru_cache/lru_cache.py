class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: "Node | None" = None
        self.previous: "Node | None" = None


class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.limit = limit
        self.cache: dict = {}  # key -> node
        self.head: Node | None = None  # most recently used
        self.tail: Node | None = None  # least recently used

    def get(self, key):
        """Look up value by key. Returns None if not found. O(1)."""
        node = self.cache.get(key)
        if node is None:
            return None
        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        """Associate value with key, evicting LRU item if at limit. O(1)."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            if len(self.cache) > self.limit:
                self._evict_tail()

    def _add_to_head(self, node: Node):
        node.next = self.head
        node.previous = None
        if self.head is not None:
            self.head.previous = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def _remove_node(self, node: Node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        node.next = None
        node.previous = None

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_to_head(node)

    def _evict_tail(self):
        if self.tail is None:
            return
        del self.cache[self.tail.key]
        self._remove_node(self.tail)