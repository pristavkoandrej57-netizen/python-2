text1 = input("Введите первый набор чисел: ")
text2 = input("Введите второй набор чисел: ")

textNum1 = text1.split()
textNum2 = text2.split()


list1 = list()
for p in textNum1:
    if '.' in p:
        list1.append(float(p))
    else:
        list1.append(int(p))

list2 = list()
for p in textNum2:
    if '.' in p:
        list2.append(float(p))
    else:
        list2.append(int(p))

print("\nРезультат")

print(list1)
print(list2)


both = list()
for n in list1:
    if n in list2 and n not in both:
        both.append(n)
print(f"В обоих наборах: {both}")


onlyOne = list()
for n in list1:
    if n not in list2 and n not in onlyOne:
        onlyOne.append(n)
        
for n in list2:
    if n not in list1 and n not in onlyOne:
        onlyOne.append(n)
print(f"Есть в одном, но нет в другом: {onlyOne}")


Both = list()
for n in list1:
    if n not in both and n not in Both:
        Both.append(n)
        
for n in list2:
    if n not in both and n not in Both:
        Both.append(n)
print(f"Все числа, кроме общих: {Both}")