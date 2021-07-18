# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8.

def monkey_trouble(a_smile, b_smile):
    if a_smile is True:
        if b_smile is True:
            return True
        else:
            return False
    if a_smile is False:
        if b_smile is False:
            return True
        else:
            return False
