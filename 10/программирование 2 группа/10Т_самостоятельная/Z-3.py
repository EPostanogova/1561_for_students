for n in range(10000):
    n_bin=bin(n)[2:]
    n_bin=n_bin+n_bin[-1:]
    c = n_bin.count("1")
    d = c%2
    n_bin = n_bin+str(d)
    r = int(n_bin) #вторым аргументом надо указывать из какой системы счисления переводим
    if r <= 13500:
        print(r) #Укажите максимальное число R, а ты n печатаешь
        break #Ищем максимальное зачем break?
