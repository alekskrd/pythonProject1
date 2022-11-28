"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях.
 Позиции хранятся в файле file.txt в одной строке одно число."""

import random


num_quant = int(input("Задайте диапазон элементов N: "))
list_quant = []
for elem in range(-num_quant, num_quant):
    list_quant.append(str(elem))

with open(r"lines.txt", "w") as file:
    for num in range(0, num_quant):
        file.write(random.choice(list_quant))
        file.write("\n")

check = True
while check:
    num_line_start = int(input("Введите позицию начала (номер строки) от 1 до N: "))
    num_line_end = int(input("Введите позицию конца (номер строки) от 1 до N: "))
    if 1 <= num_line_start < num_quant and num_line_start < num_line_end <= num_quant:
        check = False
    else:
        print("\033[31mНеверный ввод!\033[0m")

with open(r"lines.txt", "r") as file:
    mult_list = []
    for line in file:
        mult_list.append(int(line))
mult_list = mult_list[num_line_start - 1:num_line_end:1]

print(f"\033[33mДиапазон элементов с {num_line_start} по {num_line_end} строку: {mult_list}")
mult = 1
for i in mult_list:
    mult = mult * i
print(f"\033[33mПроизведение элементов: {mult}\033[0m")
