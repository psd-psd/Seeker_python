# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000

def plusMinus(arr):
    p=0
    n=0
    z=0
    for i in range(len(arr)):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n+=1
        else:
            z+=1
    return print(format(p/len(arr), '.6f')), print(format(n/len(arr), '.6f')), print(format(z/len(arr), '.6f'))
