def get_even_list(nums = []):
    new_list = []
    for index,item in enumerate(nums): 
        if item % 2 == 0:       
            # print(item)
            new_list.append(item)
    return new_list              

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
