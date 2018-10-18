def extract_even(nums = []): 
    for index ,item in enumerate(nums): 
        if nums[index] % 2 == 0:       
            print(nums[index])
                  
extract_even(nums = [1, 4, 5, -1, 10] )


