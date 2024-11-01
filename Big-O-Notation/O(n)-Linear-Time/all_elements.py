import time

def print_elements(array):
    start_time =  time.time()
    for element in array:
        time_taken = time.time() - start_time
        return element, time_taken

sizes = [10, 100, 1000, 10000, 10000, 100000]
times = []

for size in sizes:
    array = list(range(size))
    _,time_taken = print_elements(array)
    times.append(time_taken)

print(times)