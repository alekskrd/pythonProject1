"""Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.

    *Пример:*

    - 6782 -> 23
    - 0.56 -> 11"""

# num = float(input("Введите  число: "))
# while num != int(num):
#     num *= 10
# res = 0
# while num > 0:
#     res += num % 10
#     num //= 10
# print(int(res))


num = float(input("Введите число: "))
su = 0
for i in str(num):
    if i != ".":
        su += int(i)
print(su)
