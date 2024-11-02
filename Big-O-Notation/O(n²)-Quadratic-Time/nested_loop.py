def nested_function(family):
    for i in family:
        for j in family:  # Use a different loop variable here to avoid reusing 'i'
            print(j)

my_numbers = [1, 2, 3, 4, 5]            
nested_function(my_numbers)
