/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 * * Calculate the sum and product of integers in a list
 *
 * Time Complexity: O(n) - one pass over the array
 * Space Complexity: O(1) - only two variables regardless of input size
 * Optimal Time Complexity: O(n) - every element must be visited at least once
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {sum, product};
}

//console.log(calculateSumAndProduct([2, 3, 5])); 

//console.log(calculateSumAndProduct([1, 2, 3, 4]));

//console.log(calculateSumAndProduct([]));