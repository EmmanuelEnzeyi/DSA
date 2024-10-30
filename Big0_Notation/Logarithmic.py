import time
import matplotlib.pyplot as plt

def binary_search_with_timing(arr, target):
    low, high = 0, len(arr) - 1
    start_time = time.time()
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, (time.time() - start_time)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, (time.time() - start_time)

timing_results = []
array_sizes = [10, 100, 1000, 10000, 100000, 1000000]
targets = [size // 2 for size in array_sizes]

for size, target in zip(array_sizes, targets):
    arr_ = list(range(size))
    _, time_taken = binary_search_with_timing(arr_, target)
    timing_results.append(time_taken)

plt.figure(figsize=(10, 5))
plt.plot(array_sizes, timing_results, marker='o', linestyle='-', color='b')
plt.xlabel("Array Size (n)")
plt.ylabel("Time Taken (Seconds)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()
