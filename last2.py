# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    c=0
    for i in range(2,len(str)):
        if str[len(str)-2:len(str)]==str[i-2:i]:
            c+=1
    return c
