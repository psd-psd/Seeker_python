def kangaroo(x1, v1, x2, v2):
    for t in range (0, 10000):
        if (v1*t+x1)==(v2*t+x2):
            return 'YES'
    else:
        return 'NO'
