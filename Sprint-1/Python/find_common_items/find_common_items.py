from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n + m) - one pass to build Set, one pass to filter
    Space Complexity: O(n + m) - Set stores up to m items, result stores up to n
    Optimal time complexity: O(n + m) - every element must be visited at least once
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_set and item not in seen:
            common_items.append(item)
            seen.add(item)

    return common_items
