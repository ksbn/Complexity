from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n) - single pass through the list
    Space Complexity: O(n) - Set stores up to n numbers
    Optimal time complexity: O(n) - every element must be visited at least once
    """
    seen = set()
    
    for num in numbers:
        if (target_sum - num) in seen:
            return True
        seen.add(num)

    return False
