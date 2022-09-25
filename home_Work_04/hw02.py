# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
# --------------------------------------------------------------------------------------------------
def Factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans
print(Factor(int(input('Введите число: ')))) # [2, 2, 5]

# или
# n = int(input()) # 20
# while n > 1:
#     i = 2
#     f = 0
#     while 1:
#         if n%i == 0:
#             n = n // i
#             print(i, end=' ')
#             f = 1
#             break
#         else:
#             i += 1
#     if f == 1:
#         continue
# print() # 2 2 5