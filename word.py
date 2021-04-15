#program to find the number of ocurrence of a word

txt="""Golden rule of data - don't aggregate too don't don't don't early"""
a=0
for i in range(0, 12):
    if txt.split()[i]=="""don't""":
        a+=1
print(a)
