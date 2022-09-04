# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

from ast import While
from tkinter import N


fib1 = fib2 = 1
n = input('Номер ряда Фибоначи: ')
n = int(n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print('Значение этого элемента: ', fib2)
