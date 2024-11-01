# O(n) - Linear Time Complexity

**O(n) time complexity**, or **linear time complexity**, describes algorithms whose runtime grows linearly with the size of the input. This means that as the size of the input data increases, the time required to process the data increases proportionally.

## Key Points of O(n)

- **Proportional Growth**: In O(n) algorithms, if the input size doubles, the time to complete the task also roughly doubles.
- **Common in Iterative Algorithms**: O(n) is typical for algorithms that require a single pass through the data, such as searching or iterating through elements in a list.
- **Efficient for Moderate Inputs**: While linear time complexity is not the fastest, it is still efficient enough for many applications involving moderate-sized data sets.

## Examples of O(n) Algorithms

### 1. Linear Search

A simple search algorithm that checks each element in a list to find a target value has a linear time complexity of O(n).

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

- In this example, in the worst case, the algorithm checks every element once, resulting in O(n) complexity.

### 2. Finding the Maximum Value in a List

To find the maximum value in a list, you must examine each element, leading to linear time complexity.

```python
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
```

- This function requires a single traversal of the list, yielding O(n) complexity.

### 3. Counting Occurrences of an Element

Counting how many times an element appears in a list involves checking each element, resulting in linear time complexity.

```python
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
```

- The algorithm checks each item in the array, resulting in O(n) complexity.

---

## Visualizing O(n)

In an O(n) algorithm, the runtime increases directly in proportion to the input size, represented in the graph below:

```
Time
│
│        /
│      /
│    /
│  /
│/
└───────────────────
        Input Size (n)
```

## Why O(n) is Efficient

- **Simple and Intuitive**: Linear algorithms are straightforward to implement and understand.
- **Works Well for Large Inputs**: O(n) complexity allows for processing reasonably sized data sets effectively.

### Summary

O(n), or linear time complexity, describes algorithms where the time required to complete a task grows linearly with the size of the input. This complexity is common in iterative algorithms and is efficient for many practical applications.
