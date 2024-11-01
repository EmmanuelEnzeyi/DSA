# O(n log n) - Linearithmic Time Complexity

**O(n log n) time complexity**, or **linearithmic time complexity**, describes algorithms that grow slightly faster than linear time but much slower than quadratic time. This complexity is often associated with efficient sorting and divide-and-conquer algorithms.

## Key Points of O(n log n)

- **Combination of Linear and Logarithmic Growth**: O(n log n) complexity represents algorithms that perform an `O(log n)` operation `n` times.
- **Common in Sorting and Divide-and-Conquer**: Many efficient sorting algorithms, such as mergesort and heapsort, operate in O(n log n) time. It’s also common in divide-and-conquer approaches, where the problem is repeatedly split and solved in smaller parts.
- **Ideal for Moderate to Large Inputs**: O(n log n) algorithms handle large inputs efficiently, much better than O(n²) or O(2ⁿ) algorithms.

## Examples of O(n log n) Algorithms

### 1. Mergesort

Mergesort divides the array into two halves, recursively sorts each half, and then merges them, resulting in O(n log n) complexity.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
```

- Mergesort has O(n log n) complexity because it splits the list (log n divisions) and then merges them (n operations).

### 2. Heapsort

Heapsort involves building a heap from the data, then repeatedly extracting the maximum (or minimum) element and restructuring the heap. This also achieves O(n log n) complexity.

```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # O(n)
    sorted_list = []
    while arr:
        sorted_list.append(heapq.heappop(arr))  # O(log n)
    return sorted_list
```

- Building the heap takes O(n) time, and removing elements one by one takes O(log n) per removal, resulting in an overall O(n log n) time complexity.

### 3. Fast Fourier Transform (FFT)

The Fast Fourier Transform, used in digital signal processing, is an O(n log n) algorithm that efficiently computes the discrete Fourier transform of an array.

---

## Visualizing O(n log n)

In an O(n log n) algorithm, the runtime grows faster than linear but slower than quadratic. The graph would look like this:

```
Time
│
│           /
│         /
│       /
│    /
│ /
└───────────────────
        Input Size (n)
```

## Why O(n log n) is Important

- **Efficient for Sorting**: O(n log n) is the best achievable time complexity for comparison-based sorting algorithms, making it essential in computing.
- **Scalable and Practical**: O(n log n) algorithms handle large data sets more efficiently than O(n²) or higher-complexity algorithms.

### Summary

O(n log n), or linearithmic time complexity, describes algorithms that grow faster than linear but are manageable for large inputs. Understanding O(n log n) algorithms is key for working with efficient sorting and divide-and-conquer methods.
