for n in range(1,10000):
    nb=bin(n)[2:]
    if n%3==0:
        nb=nb+nb[-2:]
    else:
        ost=bin(n%3*3)[2:]
        nb=nb+ost
    r=int(nb,2)
    if r>=195:
        print(r)
        break # убери его и увидишь, что числа r не будут идти в отсортированном виде -> минимальное не самое первое