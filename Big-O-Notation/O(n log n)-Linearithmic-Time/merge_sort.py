#7 Things
#Start Function
def divide_sort_merge(the_list):
    if len(the_list)<=1:
        return the_list
    mid=len(the_list)//2
    
    left_side=the_list[:mid]
    right_side=the_list[mid:]
    
    sorted_left=divide_sort_merge(left_side)
    sorted_right=divide_sort_merge(right_side)
    
    return sort_functio(sorted_left,sorted_right)
#declare empty list
#define mid
#define left_side
#define right_side
#function recursion for left_side
#function recursion for right_side
#merge right and left side

#8 Things
#start function
def sort_functio(left,right):
    new_sorted_list=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            new_sorted_list.append(left[l])
            l=l+1
        else:
            new_sorted_list.append(right[r])
            r=r+1
    new_sorted_list.extend(left[l:])
    new_sorted_list.extend(right[r:])
    return new_sorted_list
#declare empty list
#declare indexing for j and i
#create a while loop to check if index[] values are equal  to current counter for both using len() 
#if left index greater right index append to left index
#increment index
#else if right indec greater than left, append right
#extend sorted with right
#etend sorted with left

my_list=[1,7,3,20,5,6,7,12,9,10]
final_list=divide_sort_merge(my_list)
print("final list:",final_list)
#3 Things
#sample array
#merge sort array and store
#print out