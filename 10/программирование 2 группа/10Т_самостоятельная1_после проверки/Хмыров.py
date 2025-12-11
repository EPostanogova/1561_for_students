# Задача 1
# for n in range(1000):
#     nb = bin(n)[2:]
#     if n % 3 == 0:
#        nb =str(nb)+str(nb[-2:])
#     else:
#         ost = n % 3 #то остаток от деления умножается на 3
#         ost = bin(ost)[2:]
#         nb = str(nb)+str(ost)
#     r = int(nb,2)
#     if r >= 195:
#         print(r)
#         break # убери его и увидишь, что числа r не будут идти в отсортированном виде -> минимальное не самое первое
# Ответ:202
# Задача 2

#Задача 3
for n in range(1000): #слишком маленький диапазон, зачту первый раз
    nb = bin(n)[2:]
    nb = str(nb) + str(nb)[-1:]
    summ = nb.count('1')
    ost = summ % 2
    nb = str(nb) + str(ost)
    r = int(nb,2)
    if r < 13500:
        print(r)

# Ответ: 3999