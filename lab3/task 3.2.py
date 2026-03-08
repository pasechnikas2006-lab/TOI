hlp=("calculator v0.1 by dgnz_\n \n"
      
      "Доступные операции:\n"
      "1. сложение\n"
      "2. вычитание\n"
      "3. умножение\n"
      "4. деление\n"
      "5. возведение в степень\n"
      "6. факториал числа\n"
      "7. квадратный корень из числа\n"
      "8. среднее арифметическое\n"
      "exit - выход из программы\n"
      "help - показать это сообщение снова\n"
      "----------------------------\n")
print(hlp)
def plus():
    try:
        a=float(input("слагаемое 1: "))
        b=float(input("слагаемое 2: "))
        print(f"сумма: {a + b}")
    except ValueError:
        print("некорректные данные")
def minus():
    try:
        a=float(input("уменьшаемое: "))
        b=float(input("вычитаемое: "))
        print(f"разность: {a-b}")
    except ValueError:
        print("некорректные данные")
def mult():
    try:
        a=float(input("множитель 1: "))
        b=float(input("множитель 2: "))
        print(f"произведение: {a*b}")
    except ValueError:
        print("некорректные данные")
def div():
    try:
        a = float(input("делимое: "))
        b = float(input("делитель: "))
        print(f"частное: {a / b}")
    except ValueError:
        print("некорректные данные")
    except ZeroDivisionError:
        print("на ноль делить нельзя")
def power():
    try:
        a = float(input("число: "))
        b = float(input("степень: "))
        print(f"число в степени: {a ** b}")
    except ValueError:
        print("некорректные данные")
def factorial():

    try:
        n=int(input("число: "))
        if n<0:
            raise ValueError("число не может быть отрицательным")
        x=1
        for i in range(1, n + 1):
            x = x * i
        print(f"факториал числа: {x}")
    except ValueError:
        print("некорректные данные")
def sqrt():
    try:
        a=float(input("число: "))
        if a<0:
            raise ValueError("число не должно быть отрицательным")
        print(f"корень из числа: {a ** 0.5}")
    except ValueError:
        print("некорректные данные")
def midpoint():
    try:
        a=(input("введите числа через пробел: ").split())
        x = 0
        for i in a:
            i=float(i)
            x=x+i
        y: float=x/len(a)
        print(y)
    except ValueError:
        print("некорректные данные")


dict1 = {
    1: plus,
    2: minus,
    3: mult,
    4: div,
    5: power,
    6: factorial,
    7: sqrt,
    8: midpoint
}

while True:
    num=input("выберите операцию: ")
    if num=="exit":
        break
    elif num=="help":
        print(hlp)
    else:
        try: num=int(num)
        except ValueError:
            print(f"неправильный номер операции")
            continue
        dict1[num]()





