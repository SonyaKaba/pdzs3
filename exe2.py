# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import pow

mylist = input('enter numbers : ').split()

while len(mylist) > 1:
    print(int(mylist.pop(0)) * int(mylist.pop(-1)))

if len(mylist):
    print(round(pow(int(mylist.pop(0)), 2)))

