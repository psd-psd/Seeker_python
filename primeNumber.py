n=int(input('enter the number '))
a=0
for i in range (2, n):
    a=n%i
    if a==0:
        print('the number is not prime ')
        break
    else:
        if i==n-1:
            print('the number is prime')
