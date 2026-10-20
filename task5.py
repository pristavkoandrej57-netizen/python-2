a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
def summ(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def dele(a,b):
    if(b!=0):
        return a/b
    else:
        return("Ошибка, деление на 0!")
def ostatok(a,b):
    if(b!=0):
        return a%b
    else:
        return("Ошибка, деление на 0!")
def step(a,b):
    return a**b

print(f" Сумма: {summ(a,b)} \n Вычитание: {substr(a,b)} \n Умножение: {multiple(a,b)} \n Деление: {delen(a,b)} \n Остаток: {ostat(a,b)} \n Степень: {step(a,b)}")