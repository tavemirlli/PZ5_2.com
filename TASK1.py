#Дано целое число, большее 999. Используя одну операцию деления, найти цифру, соответствующую разряду тысяч
# в записи этого числа.
a = int(input('Введите число большее 999: '))
b = a//1000
c = str(b%10)
print('Цыфра, соответствующая разряду тысяч: ', c[0])