text = input("Введите текст: ")
newText = text.split(" ")

print(f"Количество слов: {len(newText)}")

freq={}
for i in newText:
    i = i.lower()
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Частота слов:", freq)

most = max(freq, key=freq.get)
print("Самое частое слово:", most, "-", freq[most], "раз")

short = min(newText, key=len)
long = max(newText, key=len)
print("Самое короткое слово:", short)
print("Самое длинное слово:", long)

def moreThanThree(item):
    return len(item)>=3

filtered = list(filter(moreThanThree,newText))
result = "".join(filtered)
print(f"Отфильтрованная строка: {result}")

freq2 = {}
for i in filtered:
    i = i.lower()
    if i in freq2:
        freq2[i] += 1
    else:
        freq2[i] = 1

print("Частота слов:", freq2)

if freq2:
    most2 = max(freq2, key=freq2.get)
    print("Самое частое слово:", most2, "-", freq2[most2], "раз")
    print("Самое короткое слово:", min(filtered, key=len))
    print("Самое длинное слово:", max(filtered, key=len))