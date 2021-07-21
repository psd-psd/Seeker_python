# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False


def array123(nums):
    if len(nums)==0:
            return False
    else:
        for i in range(len(nums)-2):
            if nums[i]==1:
                if nums[i+1]==2:
                    if nums[i+2]==3:
                        return True
        
        return False
