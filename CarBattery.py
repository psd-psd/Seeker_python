#calculates the car battery percentage by checking the kms run

def drive(x):
    p=(100-x//6)/100*100
    if p>=20:
        print('The battery percentage remaning is',p,'%',"and you are good to go")
    elif p<=0:
        print('you have run out of charge and the vehicle cant move')
    else:
        print('Alert!! The battery percentage is', p,'%',"too low please recharge")
