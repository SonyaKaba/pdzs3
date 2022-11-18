# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

fib1 = 1
fib2 = 1
 
n = input("element number of the fibonacci series: ")
n = int(n)
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print("element = ", fib2)