import matplotlib.pyplot as plt
import time

def get_first_element(arr):
    return arr[0]

sizes = [10, 100, 1000, 10000, 100000, 1000000]
times = []

for size in sizes:
    arr = list(range(size))
    start_time = time.time()
    get_first_element(arr)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot the times for each input size
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', label="O(1) Time")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity of O(1) Operation")
plt.grid(True)
plt.legend()
plt.show()