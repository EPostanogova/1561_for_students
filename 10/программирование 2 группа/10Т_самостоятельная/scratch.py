

for a in range(1000):
    a_bin=bin(a)[2:]
    if a % 3 == 0:
        a_bin = a_bin+a_bin[-2:]
    else:
        d = a%3
        c = d * 3
        c = bin(c)[2:]
        a_bin = a_bin + c
    r =  int(a_bin, 2)
    if r >= 195:
        print(a) #Укажите минимальное число R, а ты печатаешь n
        break # убери его и увидишь, что числа r не будут идти в отсортированном виде -> минимальное не самое первое

