from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
   
    """
    #Calculate the sum and product of integers in a list.

    #Time Complexity: O(n) - single pass through the list
    #Space Complexity: O(1) - only two variables regardless of input size
    #Optimal time complexity: O(n) - every element must be visited at least once
    
    # Edge case: empty list
    total = 0
    product = 1

    for current_number in input_numbers:
        total += current_number
        product *= current_number

    return {"sum": total, "product": product}
