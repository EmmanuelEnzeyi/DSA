# sum all elements in an array
# create a function that takes an array as argument and dsums all elements in an array
def sum_array_elements(array):
    total = 0
    for element in array:
        total += element
    return total
# create array sizes
sizes = [10, 100]
# create the summations array to hold different summations for different array sizes
summations = []
# create a for loop to create the arrays and pass then iteratibely to the function
for size in sizes:
    array = list(range(size))
    print(array)
    sums = sum_array_elements(array)
    summations.append(sums)
# in the for loop append all the summations summations
# print the summations to console
print(summations)