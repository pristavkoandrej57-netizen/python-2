BasicPlan = 24.99
min = int(input("Введите количество минут разговоров: "))
message = int(input("Введите количество сообщений: "))
internet = int(input("Введите количество Мб интернета: "))
BasicMin = 0.89
BasicMessage = 0.59
BasicInternet = 0.79

extraMinCost = 0
extraMessageCost = 0
extraInternetCost = 0

if min > 60:
    print("Дополнительные разговоры!")
    for i in range(60, min):
        extraMinCost += BasicMin
    print(f"  Доплата за минуты: {extraMinCost:.2f} руб.")

if message > 30:
    print("Дополнительные сообщения!")
    for i in range(30, message):
        extraMessageCost += BasicMessage
    print(f"  Доплата за SMS: {extraMessageCost:.2f} руб.")

if internet > 1024:
    print("Дополнительный интернет!")
    for i in range(1024, internet):
        extraInternetCost += BasicInternet
    print(f"  Доплата за интернет: {extraInternetCost:.2f} руб.")

subtotal = BasicPlan + extraMinCost + extraMessageCost + extraInternetCost
fee = subtotal * 0.02
total = subtotal + fee

print(f"Стоимость услуг: {total:.2f} руб.")