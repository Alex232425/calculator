solo = input("Выберите символ (+,-,*,/,**,%): ")

a = float(input("Введите первый символ: "))
b = float(input("Введите второй символ: "))

if solo == "+":
    c = a+b
    print("Результат: " + str(c))
elif solo == "-":
    c = a-b
    print("Результат: " + str(c))
elif solo =="*":
    c = a*b
    print("Результат: " + str(c))
elif solo =="/":
    c = a/b
    print("Результат: " + str(c))
elif solo =="**":
    c = a**b
    print("Результат: " + str(c))
elif solo == "%":
    c = a % b
    print("Результат: " + str(c))
else:
    print("Неправильный выбор!")