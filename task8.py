import random
numberRand = random.randint(1,100)
cont = True
while(cont):
    guess = int(input("Введите число: "))
    if(guess < numberRand):
        print(f"Загаданное число больше {guess}")
    elif(guess > numberRand):
        print(f"Загаданное число меньше {guess}")
    else:
        print(f"Загаданное число {guess}!")
        cont = False
    