Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True


def pos_neg(a, b, negative):
    if a<0:
        if b<0:
            if negative is True:
                return True
            else:
                return False
        elif b>0:
            if negative is True:
                return False
            else:
                return True
    elif a>0:
        if b<0:
            if negative is True:
                return False
            else:
                return True
        if b>0:
            return False
