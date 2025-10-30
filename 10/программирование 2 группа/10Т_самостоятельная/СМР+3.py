for n in range(1,10000):
    nb=bin(n)[2:]
    nb=nb+nb[-1]
    ost=nb.count('1')%2
    nb=nb+str(ost)
    r=int(nb,2)
    if r<13500:
        print(r)