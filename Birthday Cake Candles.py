# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example


# The maximum height candles are  units high. There are  of them, so return .

# Function Description

# Complete the function birthdayCakeCandles in the editor below.

# birthdayCakeCandles has the following parameter(s):

# int candles[n]: the candle heights
# Returns

# int: the number of candles that are tallest
# Input Format

# The first line contains a single integer, , the size of .
# The second line contains  space-separated integers, where each integer  describes the height of .

# Constraints

# Sample Input 0

# 4
# 3 2 1 3
# Sample Output 0

# 2

def birthdayCakeCandles(candles):
    c=0
    candles.sort(reverse = True)
    try:
        for i in candles:
            if i==candles[0]:
                c+=1
            else:
                break
    except:
        TypeError
    return c
