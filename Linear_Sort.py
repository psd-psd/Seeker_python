#sorting an array by mean method

we=[2 ,3, 5, 7, 1, 9, 3, 8, 0, 4]
avg=sum(we)/2
left=[]
right=[]
i,j=0,0
while j<len(we):
    if we[i]<avg:
        left.append(i)
    else:
        right.append(i)
    j+=1 
    i+=1
 print(left+right)
