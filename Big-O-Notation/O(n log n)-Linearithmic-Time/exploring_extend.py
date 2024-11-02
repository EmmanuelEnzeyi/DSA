def exploring_extend(arr): 
    arr=[] 
    mid=len(arr)//2 
    left_side=arr[:mid] 
    right_side=arr[mid:]
    left_side.extend(right_side)
    return left_side  

my_array=[1,2,3,4,5,6,7,8,9,10] 
exploring_extend(my_array)