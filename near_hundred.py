# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
    if n<90:
        return False
    elif n>210:
        return False
    elif abs(100-n)<=10:
        return True
    elif abs(100-n)>=190:
        if abs(100-n)<=210:
            return True
        else:
            return False
    elif abs(100-n)>=90:
        if abs(100-n)<=110:
            return True
        else:
            return False
    else:
        return False
