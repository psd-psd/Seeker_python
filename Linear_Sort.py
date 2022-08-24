#sorting an array by mean method

we=[10, 14, 28, 11, 7, 16, 30, 50, 25, 18].
for i in range(0,len(we)):
    for j in range(i+1,len(we)):
        if we[i]>we[j]:
            temp=we[i]
            we[i]=we[j]
            we[j]=temp
print(we)
