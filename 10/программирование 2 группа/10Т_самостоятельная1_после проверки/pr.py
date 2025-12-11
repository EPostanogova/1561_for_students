for n in range(1,1000):
    nb=bin(n)[2:]
    if n%3==0:
        nb = nb + nb[-2:]
    else:
        nb = nb + bin(n%3*3)[2:]
    r=int(nb, 2)
    if r>=195:
        print(r)

def f(n):
    x=''
    while n>0:
        x=str(n%4)+x
        n=n//4
    return x

for n in range(1,1000):
    nf=f(n)
    if n%4==0:
        nf='2'+nf+"03"
    else:
        nf= nf+f(n%4*5)
    r=int(nf,4)
    if r<=567:
        print(n)