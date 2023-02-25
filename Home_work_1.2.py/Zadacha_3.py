'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

N = int(input('Введите число N: '))
k = 1
number = 2**k
while number <= N:
    number = 2**k
    k +=1
    if number > N:
        break
    print(number)
