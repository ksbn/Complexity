from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n) - single pass through the sequence
    Space complexity: O(n) - Set and result list each store up to n elements
    Optimal time complexity: O(n) - every element must be visited at least once
    """
    seen = set()
    unique_items = []

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)

    return unique_items