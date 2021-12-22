def whoisthewinner(x):
    while 1:
        print('a pls enter num')
        a=int(input())
        x=x-a
        if x<=0:
            print('A is the winner')
            break
        print('b pls enter num')
        b=int(input())
        x=x-b
        if x<=0:
            print('B is the winner')
            break
            
            
            
            
def whoisthewinner(x):
    if (x-x%9)%2==0 and x%9>0:
        print('A is the winner')
    elif (x-x%9)%2==0 and x%9==0:
        print('B is the winner')
    elif (x-x%9)%2!=0 and x%9==0:
        print('A is the winner')
    elif (x-x%9)%2!=0 and x%9>0:
        print('B is the winner')
