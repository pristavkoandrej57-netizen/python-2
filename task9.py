print("Категории: длина, масса, время")
pick = input("Введите категорию: ").lower()

if pick == "длина":
    print("Единицы: м, км, миля")
    from_unit = input("Из какой единицы: ").lower()
    to_unit = input("В какую единицу: ").lower()
    value = float(input("Введите значение: "))

    if from_unit == "м":
        base = value
    elif from_unit == "км":
        base = value * 1000
    else:
        base = value * 1609.344

    if to_unit == "м":
        result = base
    elif to_unit == "км":
        result = base / 1000
    else:
        result = base / 1609.344

    print(f"{value} {from_unit} = {result:.6g} {to_unit}")

elif pick == "масса":
    print("Единицы: кг, фунт")
    from_unit = input("Из какой единицы: ").strip()
    to_unit = input("В какую единицу: ").strip()
    value = float(input("Введите значение: "))

    if from_unit == "кг":
        base = value
    else:
        base = value * 0.453592  

    if to_unit == "кг":
        result = base
    else:
        result = base / 0.453592 

    print(f"{value} {from_unit} = {result:.6g} {to_unit}")

elif pick == "время":
    print("Единицы: сек, мин, час")
    from_unit = input("Из какой единицы: ").strip()
    to_unit = input("В какую единицу: ").strip()
    value = float(input("Введите значение: "))

    if from_unit == "сек":
        base = value
    elif from_unit == "мин":
        base = value * 60
    else:
        base = value * 3600

    if to_unit == "сек":
        result = base
    elif to_unit == "мин":
        result = base / 60
    else:
        result = base / 3600

    print(f"{value} {from_unit} = {result:.6g} {to_unit}")

else:
    print("Неизвестная категория")