def countApplesAndOranges(s, t, a, b, apples, oranges):
    appple_count=0
    orange_count=0
    for x in apples:
        if (a+x)>=s and (a+x)<=t:
            appple_count+=1
    for y in oranges:
        if (b+y)>=s and (b+y)<=t:
            orange_count+=1
    print(appple_count)
    print(orange_count)
