
def get_max_element(array):
    max_element = array[0]
    for element in array:
        if element > max_element:
            max_element = element
    return max_element

array = [1, 2, 3, 4, 5, 6]

max_element = get_max_element(array)
print(max_element)