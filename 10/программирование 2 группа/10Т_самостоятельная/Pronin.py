# # 1
n = 0
r = 0
while r<= 151: #Укажите минимальное число R, большее 151?
    n += 1
    x = bin(n)[2:]
    if int(x,2) % 3 == 0: #посмотри что возвращает int(x)
        x += x[-3:]
    else:
        x += bin(int(x,2) % 3 * 3)[2:]
    r = int(x, 2)
    print(n, r)
# # Ответ 155 при N = 19
# =======================================
# #2
# n = 0
# r = 0
# while r <= 60:
#     n += 1
#     x = bin(n)[2:]
#     x += str(x.count('1') % 2)
#     x += str(x.count('1') % 2)
#     r = int(x, 2)
#     print(n, r)
# # Ответ 66 при N = 16
# =======================================
# # #3
# def trio(n):
#     if n == 0:
#         return '0'
#     a = []
#     while n > 0:
#         a.append(str(n % 3))
#         n //= 3
#     return "".join(a[::-1])
#
# n = 100
# r = 200
# while r >= 199:
#     n -= 1
#     x = n
#     x = trio(x)
#     if not int(x) % 3:
#         x = '1' + x + '02'
#     else:
#         x += trio(int(x) % 3 * 4)
#     r = int(x, 3)
#     print(n, r)
# # Ответ 20