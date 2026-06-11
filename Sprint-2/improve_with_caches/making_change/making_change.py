from typing import List, Dict, Tuple

def ways_to_make_change(total: int) -> int:
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], 0, {})


def ways_to_make_change_helper(total: int, coins: List[int], index: int, cache: Dict[Tuple[int, int], int]) -> int:
    if total == 0:
        return 1
    if total < 0 or index == len(coins):
        return 0

    key = (total, index)
    if key in cache:
        return cache[key]

    coin = coins[index]

    # option 1: take coin (stay on same index)
    take = ways_to_make_change_helper(total - coin, coins, index, cache)

    # option 2: skip coin
    skip = ways_to_make_change_helper(total, coins, index + 1, cache)

    cache[key] = take + skip
    return cache[key]