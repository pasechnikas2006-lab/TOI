num = input("введите число: ")
if num.isdigit():
    num = int(num)
    if num % 2 == 0 : print("Число чётное")
    else: print("Число нечётное")
else: print("Введено не число")