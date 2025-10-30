def f(n):
    x = ''
    while n > 0:
        x = str(n % 4) + x
        n = n // 4
    return x
for n in range(1,10000):
    nf=f(n)
    if n%4==0:
        nf='2'+nf+'03'
    else:
        ost=n%4*5
        ostf=f(ost)
        nf=nf+ostf
    r=int(nf,4)
    if r<=567:
        print(n)

