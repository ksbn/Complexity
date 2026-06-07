/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n) - single pass through the array
 * Space Complexity: O(n) - Set stores up to n numbers
 * Optimal Time Complexity: O(n) - every element must be visited at least once
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  
  for (const num of numbers) {
    if (seen.has(target - num)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}
