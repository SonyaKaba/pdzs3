# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import sample


def sum_even_items(items):
    summary = 0
    for key, value in enumerate(items):
        if not key % 2 and not key == 0:
            summary = summary + value
    return summary


n = int(input('enter array size : '))
mylist = sample(range(1, 10), n)
print("Generated sequence: {}".format(mylist))
print(sum_even_items(mylist))