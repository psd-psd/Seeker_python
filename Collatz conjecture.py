#function ruturns the number of iterations required to reach 1
#inspiration from the collatz conjencture

def leaf(n):
    c=0
    while n!=1:
        c+=1
        if n%2!=0:
            n=3*n+1
        elif n%2==0:
            n=n/2
    return c
