n=int(input('enter the number '))
a=0
b=2
for i in range (b, n):
    a=n%b
    if a==0:
        print('the number is not prime ')
        break
    else:
        if a!=0:
            b=b+1
            if b==n-1:
                print('the number is prime')
