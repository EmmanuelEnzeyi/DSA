def match_elements(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return f"Match found at {i} and {j}"
    return "No matches found 😞"

# Example usage
fruit = ["🍓", "🍐", "🍊", "🍌", "🍍", "🍑", "🍎", "🍈", "🍊", "🍇"]
print(match_elements(fruit))  # "Match found at 2 and 8"