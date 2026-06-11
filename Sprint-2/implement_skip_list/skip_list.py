from __future__ import annotations
import random
from typing import Optional

class Node:
    def __init__(self, value, levels: int):
        self.value = value
        self.next: list[Optional[Node]] = [None] * levels

class SkipList:
    MAX_LEVELS = 16
    PROMOTION_PROBABILITY = 0.5

    def __init__(self):
        self.head = Node(None, self.MAX_LEVELS)
        self.current_levels = 1

    def _random_levels(self) -> int:
        levels = 1
        while (
            random.random() < self.PROMOTION_PROBABILITY
            and levels < self.MAX_LEVELS
        ):
            levels += 1
        return levels

    def insert(self, value) -> None:
        update: list[Optional[Node]] = [None] * self.MAX_LEVELS
        current = self.head

        for level in range(self.current_levels - 1, -1, -1):
            while True:
                nxt = current.next[level]
                if nxt is None or nxt.value >= value:
                    break
                current = nxt
            update[level] = current

        levels = self._random_levels()

        if levels > self.current_levels:
            for level in range(self.current_levels, levels):
                update[level] = self.head
            self.current_levels = levels

        new_node = Node(value, levels)
        for level in range(levels):
            prev = update[level]
            if prev is not None:
                new_node.next[level] = prev.next[level]
                prev.next[level] = new_node

    def __contains__(self, value) -> bool:
        current = self.head

        for level in range(self.current_levels - 1, -1, -1):
            while True:
                nxt = current.next[level]
                if nxt is None or nxt.value >= value:
                    break
                current = nxt

        nxt = current.next[0]
        return nxt is not None and nxt.value == value

    def to_list(self) -> list:
        result = []
        current = self.head.next[0]
        while current is not None:
            result.append(current.value)
            current = current.next[0]
        return result