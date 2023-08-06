# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = num1 = int(input("Введите число: "))
res_16 = ""

if num == 0:
    res_16 = "0"
else:
    while num > 0:
        if num % 16 == 10:
            res = "a"
        elif num % 16 == 11:
            res = "b"
        elif num % 16 == 12:
            res = "c"
        elif num % 16 == 13:
            res = "d"
        elif num % 16 == 14:
            res = "e"
        elif num % 16 == 15:
            res = "f"
        else:
            res = str(num % 16)
        res_16 = res + res_16
        num = num // 16
print(res_16, hex(num1).replace("0x", ""))