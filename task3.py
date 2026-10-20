price = int(input("Введите сумму в рублях: "))
if(price <0):
    print("Отрицательное значение!")
else:
    hundred = price//100
    price %= 100

    fiftie = price//50 
    price %= 50

    ten = price//10
    price %= 10

    five = price //5
    price %= 5

    two = price//2
    price %= 2

    one = price
    
    print(f"100 руб: {hundred}")
    print(f"50 руб:  {fiftie}")
    print(f"10 руб:  {ten}")
    print(f"5 руб:   {five}")
    print(f"2 руб:   {two}")
    print(f"1 руб:   {one}")
    
    