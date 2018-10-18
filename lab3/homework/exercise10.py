def get_even_list(nums = []): 
    for index ,item in enumerate(nums): 
        if nums[index] % 2 == 0:       
            print(nums[index])
    return nums[index]              

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
