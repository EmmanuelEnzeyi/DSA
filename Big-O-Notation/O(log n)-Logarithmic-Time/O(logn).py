import matplotlib.pyplot as plt
import time


def binary_search_with_timing(arr, target):
    low, high = 0, len(arr) - 1
    start_time = time.time()
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            # time_taken = time.time() - start_time
            # return mid, time_taken * 1000
            return mid, (time.time() - start_time)
        elif arr[mid] < target :
            low = mid + 1
        else:
            high = mid - 1
    return -1, (time.time() - start_time)
            
timing_results = []
array_sizes = [10, 100, 1000, 10000, 100000, 1000000, 100000000]
targets = [size // 2 for size in array_sizes]

for size, target in zip(array_sizes, targets):
    arr_ = list(range(size))
    _, time_taken = binary_search_with_timing(arr_, target)
    timing_results.append(time_taken)

print(timing_results)

# Plotting results to visualize time taken vs. array size
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, timing_results, marker='o', linestyle='-', color='g')
plt.xlabel("Array Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Binary Search Time Taken vs Array Size")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()