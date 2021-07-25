def staircase(n):
    for i in range (1,n):
         print(' '*(n-i-1),'#'*i)
    print('#'*(i+1))
