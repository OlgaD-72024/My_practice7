first = int(input("Введите целое число: "))
second = int(input("Введите целое число: "))
third = int(input("Введите целое число: "))
if first == second and first == third:
    print("Совпадений: ", 3)
elif first == second:
    print("Совпадений: ", 2)
elif first == third:
    print("Совпадений: ", 2)
elif second == third:
    print("Совпадений: ", 2)
elif first != second:
    print("Совпадений: ", 0)
elif first != third:
    print("Совпадений: ", 0)
elif second != third:
    print("Совпадений: ", 0)
else:
    print()
