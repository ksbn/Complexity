from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

class LinkedList:
    def __init__(self):
        self.head = None  # most recently pushed
        self.tail = None  # least recently pushed

    def push_head(self, value):
        """Add element to the start of the list. Returns the node (handle) for future remove()."""
        node = Node(value)
        if self.head is None:
            # List was empty
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        return node

    def pop_tail(self):
        """Remove and return the value from the end of the list."""
        if self.tail is None:
            return None
        value = self.tail.value
        self.remove(self.tail)
        return value

    def remove(self, node):
        """Remove a node from the list using the handle returned by push_head()."""
        if node.previous is not None:
            node.previous.next = node.next
        else:
            # Node is the head
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            # Node is the tail
            self.tail = node.previous

        # Clean up the node's pointers
        node.next = None
        node.previous = None