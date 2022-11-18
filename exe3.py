# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов

from random import uniform


def random_float_list(n):
    res = []
    for i in range(n):
        res.append(str(round(uniform(1,10), 2)))
    return res

n = int(input('enter array size : '))
generated_list = random_float_list(n)
print("Generated list: {}".format(generated_list))
decimals = []
for i in generated_list:
    decimals.append(int(i.split(".")[1]))

print(max(decimals) - min(decimals))
# mylist = sample(range(1, 10), n)
# print(mylist)

# max = 0
# min = 0
# for i, v in enumerate(mylist):
#     if v %  > 0:
#     max = v 
