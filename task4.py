text = input("Введите строку: ")
text2 = ""
for i in reversed(text):
    text2+=i
if(text == text2):
    print("Палиндром!")
else:
    print("Не палиндром!")