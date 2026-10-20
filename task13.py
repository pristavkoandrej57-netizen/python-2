
text = input("Введите числа: ")
textNum = text.split()


numbers = list()
floats = list()
for n in textNum:
    if '.' in n:
        floats.append(float(n))
    else:
        numbers.append(int(n))

print("\nРезультат")


uniq = list()
for n in numbers:
    if numbers.count(n) == 1:
        uniq.append(n)
print(f"Уникальные: {uniq}")


rep = list()
for n in numbers:
    if numbers.count(n) > 1 and n not in rep:
        rep.append(n)
print(f"Повторяющиеся: {rep}")

even = list()
odd = list()
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(f"Четные:{even}")
print(f"Нечетные: {odd}")


neg = list()
for n in numbers:
    if n < 0:
        neg.append(n)
print(f"Отрицательные: {neg}")


print(f"Float числа: {floats}")


total5 = 0
for n in numbers:
    if n % 5 == 0:
        total5 += n
print(f"Сумма кратных 5: {total5}")


print(f"Максимум:{max(numbers)}")
print(f"Минимум: {min(numbers)}")