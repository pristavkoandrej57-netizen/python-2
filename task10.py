from datetime import datetime
price = int(input("Введите цену товара: "))
age = int(input("Введите свой возраст: "))
birthDay = int(input("Введите свой день рождения: "))
birthmonth = int(input("Введите свой месяц рождения: "))
status = input("Введите статус: ").lower()

current = datetime.now()

if(status=="vip"):
    price=price-(price*0.15)
    
elif(price > 1000):
    price = price-(price*0.1)
    if(age >= 63):
        price = price-(price*0.05)
    if(birthDay == current.day and birthmonth == current.month):
        price = price-(price*0.05)

print(f"Итоговая цена: {price:.2f}")