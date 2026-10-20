age = int(input("Введите возраст заещика: "))
monthSal = float(input("Введиет ежемесячный доход: "))
credit = float(input("Введите размер кредита: "))
credTime = int(input("Введите срок кредита: "))
credHistory = input("Введите кредитную историю: ").lower()
Poluch = input("Наличие поручителей: ").lower()
Zalog = input("Наличие залога: ").lower()

if(age < 18):
    print("НЕСОВЕРШЕННОЛЕТНИЙ ЧЕЛОВЕК!")

#Кредит к доходу

payment = credit/credTime
credToPay = payment/monthSal

#Уровень риска

if credToPay > 0.7 or credHistory =="плохая":
    risk = "критический"
elif credToPay > 0.5 or credHistory =="удовлетворительная":
    risk = "высокий"
elif credToPay > 0.3 or credHistory =="хорошая":
    risk = "средний"
else:
    risk="низкий"
    
# Предложить процентную ставку
if risk == "низкий":
    rate = 12
elif risk == "средний":
    rate = 16
elif risk == "высокий":
    rate = 21
else:
    rate = 27
#Дать рекомендации по одобрению/отклонению

if risk =="плохая":
    decision = "ОТКЛОНИТЬ"
elif risk =="низкий":
    decision = "ОДОБРИТЬ"
else:
    decision="ОДОБРИТЬ С ОГРАНИЧЕНИЯМИ"
    
    
print(f"\nDTI: {credToPay:.2f}")
print(f"Риск: {risk}")
print(f"Ставка: {credToPay}%")
print(f"Решение: {decision}")
    

    
if not(risk == "низкий"):
    print("Рекомендации:")
    if not Zalog.lower() == "да":
        print(" - Оформить залог")
    if not Poluch.lower() == "да":
        print(" - Привлечь поручителей")
    if risk == "критический":
        print(" - Отказать в кредите")

    