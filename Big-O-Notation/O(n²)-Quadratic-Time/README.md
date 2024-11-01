# O(n²) - Quadratic Time Complexity

**O(n²) time complexity**, or **quadratic time complexity**, describes algorithms whose runtime grows quadratically with the size of the input. This means that if the input size doubles, the time to complete the task increases by four times (since \(2^2 = 4\)).

## Key Points of O(n²)

- **Squared Growth**: In O(n²) algorithms, the time taken is proportional to the square of the size of the input data.
- **Common in Nested Loops**: Quadratic time complexity often arises in algorithms that use nested loops, where each element in one loop is compared with every element in another.
- **Inefficient for Large Inputs**: Due to the rapid growth of O(n²), these algorithms can become impractical for larger datasets.

## Examples of O(n²) Algorithms

### 1. Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. It has a worst-case time complexity of O(n²).

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

- In the worst case, every element must be compared with every other element, leading to O(n²) complexity.

### 2. Selection Sort

Selection Sort is another simple sorting algorithm that divides the input list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part, which results in O(n²) complexity.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

- Each iteration involves a nested loop that goes through the remaining unsorted elements, resulting in O(n²) complexity.

### 3. Insertion Sort

Insertion Sort builds the sorted array one item at a time, taking each element from the input and finding its proper position in the sorted part. In the worst case, this also has O(n²) complexity.

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

- The inner loop in this algorithm results in O(n²) complexity when the list is sorted in reverse order.

---

## Visualizing O(n²)

In an O(n²) algorithm, the runtime grows quadratically as shown in the graph below:

```
Time
│
│              /
│            /
│          /
│        /
│      /
│    /
│  /
│/
└───────────────────
        Input Size (n)
```

## Why O(n²) Can Be Limiting

- **Performance Issues**: O(n²) algorithms can become very slow with larger datasets due to their quadratic growth.
- **Consider Alternative Algorithms**: For sorting or similar tasks, consider using more efficient algorithms like mergesort or quicksort, which operate in O(n log n) time.

### Summary

O(n²), or quadratic time complexity, describes algorithms where the time required to complete a task grows quadratically with the size of the input. These algorithms are often associated with nested loops and can become impractical for large inputs due to their inefficient growth.
