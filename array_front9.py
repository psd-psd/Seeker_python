# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
    c=0
    if len(nums)==0:
            return False
    else:
        for i in nums:
            c+=1
            if i ==9 :
                return True
            if c==4:
                return False
        return False
    
    
#     another method

def array_front9(nums):
    c=0
    if len(nums)==0:
            return False
    else:
        for i in range(0,4):
            try:
                if nums[i] ==9 :
                    return True
            except:
                IndexError
        return False
