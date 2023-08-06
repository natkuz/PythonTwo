# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

x1 = int(input("Введите числитель первой дроби: "))
x2 = int(input("Введите знаменатель первой дроби: "))
y1 = int(input("Введите знаменатель второй дроби: "))
y2 = int(input("Введите знаменатель второй дроби: "))

product_numerators = x1 * y1
pn = product_numerators
product_enominators = x2 * y2
pe = product_enominators

while product_numerators != 0 and product_enominators != 0:
    if product_numerators > product_enominators:
        product_numerators = product_numerators % product_enominators
    else:
        product_enominators = product_enominators % product_numerators
pn = pn // (product_numerators + product_enominators)
pe = pe // (product_numerators + product_enominators)
if pe != 1:
    print("Произведение дробей =", end=' ')
    print(int(pn), '/', int(pe), sep='')
else:
    print("Произведение дробей =", end=' ')
    print(int(pn))

if x2 == y2:
    sum_numerators = x1 + y1
    common_denominator = y2
else:
    x3 = x1 * y2
    common_denominator = x2 * y2
    y3 = y1 * x2
    sum_numerators = x3 + y3

cd = common_denominator
sn = sum_numerators

while sum_numerators != 0 and common_denominator != 0:
    if sum_numerators > common_denominator:
        sum_numerators = sum_numerators % common_denominator
    else:
        common_denominator = common_denominator % sum_numerators
cd = cd // (sum_numerators + common_denominator)
sn = sn // (sum_numerators + common_denominator)

if pe != 1:
    print("Сумма дробей =", end=' ')
    print(int(sn), '/', int(cd), sep='')
else:
    print("Сумма дробей =", end=' ')
    print(int(sn))

z1 = fractions.Fraction(x1, x2)
z2 = fractions.Fraction(y1, y2)
print(f'Проверка. Произведение дробей = {z1 * z2}')
print(f'Проверка. Сумма дробей = {z1 + z2}')
