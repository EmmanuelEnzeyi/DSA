# Common Big O Notations

## O(1) - Constant Time Complexity
- The algorithm's runtime remains constant regardless of the input size.
- **Example**: Accessing an element in an array by index.

## O(log n) - Logarithmic Time Complexity
- The runtime increases logarithmically as the input size grows.
- **Example**: Binary search, where the problem size halves each time.

## O(n) - Linear Time Complexity
- The runtime grows linearly with the input size.
- **Example**: Iterating through an array once.

## O(n log n) - Linearithmic Time Complexity
- Slightly more complex than linear, common in efficient sorting algorithms.
- **Example**: Merge sort, quicksort (average case).

## O(n²) - Quadratic Time Complexity
- The runtime grows proportionally to the square of the input size.
- **Example**: Nested loops in a bubble sort for an array.

## O(n³) - Cubic Time Complexity
- The runtime grows proportionally to the cube of the input size.
- **Example**: Triple nested loops, often found in certain matrix operations.

## O(2ⁿ) - Exponential Time Complexity
- The runtime doubles with each additional element in the input.
- **Example**: Recursive algorithms for the Fibonacci sequence, brute-force combinatorial problems.

## O(n!) - Factorial Time Complexity
- The runtime grows factorially with the input size.
- **Example**: Generating all permutations of a list.

---

## Using Big O Notation

Big O notation provides a way to analyze algorithms for:

- **Best Case**: Optimistic scenario.
- **Worst Case**: Pessimistic scenario.
- **Average Case**: Expected behavior for random input.

Most Big O analyses focus on the worst-case scenario to ensure that the algorithm performs within acceptable limits under any condition.
