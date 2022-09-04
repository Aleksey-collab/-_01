# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

#fib1 = fib2 = 1
#n = input('номер элемента ряда Фибоначи: ')
#n = int(n)
#
#i = 0
#while i < n - 2:
#    fib_sum = fib1 + fib2
#    fib1 = fib2
#    fib2 = fib_sum
#    i = i + 1
#
#print('Значение этого элемента: ', fib2)



fib1 = fib2 = 1
n = int(input('номер элемента ряда Фибоначи: '))

print(fib1, fib2, end =' ')

for i in range (2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = ' ') 