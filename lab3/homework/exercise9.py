def extract_even(nums = []):
    new_list = [] 
    for index ,item in enumerate(nums): 
        if item % 2 == 0:       
            new_list.append(item)
    return new_list        
                  
print(extract_even(nums = [1, 4, 5, -1, 10] ))



