/**
* Finds common items between two arrays.
 *
 * Time Complexity: O(n + m) - one pass to build the Set, one pass to filter
 * Space Complexity: O(n + m) - Set stores up to m items, result stores up to n
 * Optimal Time Complexity: O(n + m) - every element must be visited at least once
 *
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};
