#для второй задачи
def zov(u):
    x = ''
    while u != 0:
        x = str(u%4)+x
        u = u//4
    return x
#Первая задача
for n in range(1,1000):
    nb = bin(n)[2:]
    if n%3==0:
        nb = nb + nb[-2:]
    else:
        b = n%3*3
        b = bin(b)[2:]
        nb = nb+b
    r = int(nb,2)
    if r >= 195:
        print(r)
        break # убери его и увидишь, что числа r не будут идти в отсортированном виде -> минимальное не самое первое

#Вторая задача
for u in range(1,1000):
    nb = zov(u)
    if u %4 == 0:
        nb = "2" + nb + "03"
    else:
        b = zov(u%4*5)
        nb = nb + b
    r = int(nb,4)
    if r <= 567:
        print(u)
#Третья задача
for y in range(1,10000):
    nb = bin(y)[2:]
    nb = nb + nb[-1]
    nb = nb + str(nb.count("1")%2)
    r = int(nb,2)
    if r <= 13500:
        print(r)


