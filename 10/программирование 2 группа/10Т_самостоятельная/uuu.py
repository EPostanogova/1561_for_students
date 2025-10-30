def r(n):
    b=bin(n)[2:]
    if n%3:
        b = b+bin(n%3*3)[::2]
    else:
        b = (b%3*3)
        b = bin(b)[::n]
    int(b,2)
    print(b)
