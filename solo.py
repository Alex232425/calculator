
choose =input("Выберите символ: (+,-)")

a = int(input("Введите первый символ: "))
b = int(input("Введите второй символ: "))

if choose == "+":
    c = a+b

    print("Результат: " + str(c))
elif choose == "-":
    c = a-b
    print("Результат: " + str(c))

else:
    print("Неправильный выбор!")