# O(log n) - Logarithmic Time Complexity

**O(log n) time complexity**, or **logarithmic time complexity**, describes algorithms where the runtime grows logarithmically as the input size increases. This means that as `n` grows, the time required grows much slower in comparison, making logarithmic algorithms very efficient for large inputs.

## Key Points of O(log n)

- **Substantial Efficiency**: O(log n) algorithms perform very well on large data sets because each operation significantly reduces the problem size.
- **Dividing Problem in Halves**: Logarithmic time complexity often appears in algorithms that divide the data set in half with each iteration, such as binary search.
- **Common in Search and Divide and Conquer Algorithms**: Frequently found in searching algorithms, such as binary search, or in divide-and-conquer strategies, like mergesort’s recursive halving.

## Examples of O(log n) Algorithms

### 1. Binary Search

Binary search divides the search space in half each time, reducing the number of operations logarithmically.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

- In binary search, each comparison halves the search space, resulting in O(log n) complexity.

### 2. Finding Powers of a Number (Exponentiation by Squaring)

Efficiently computing large powers of a number by repeatedly squaring can reduce the problem size logarithmically.

```python
def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result
```

- This technique, known as **exponentiation by squaring**, allows calculating large powers with O(log n) operations.

### 3. Tree Traversals in Balanced Trees

Traversing a balanced binary search tree (BST) can also operate in logarithmic time for lookups, insertions, and deletions due to the tree’s balanced structure.

---

## Visualizing O(log n)

In an O(log n) algorithm, the runtime increases slowly as input size grows. The graph below demonstrates this:

```
Time
│
│      ┌─────────
│     /
│   /
│ /
│──────────────────
        Input Size (n)
```

## Why O(log n) is Efficient

- **Scalable for Large Inputs**: Because O(log n) algorithms grow slowly, they’re highly efficient and scalable.
- **Reduced Operations**: O(log n) complexity means fewer operations as the problem size increases, often due to halving the data set in each step.

### Summary

O(log n), or logarithmic time complexity, describes algorithms that reduce the input size by half with each step. These algorithms are efficient and well-suited for large inputs, commonly appearing in searching and divide-and-conquer problems.
