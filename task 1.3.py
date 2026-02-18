age = input("Введите свой возраст: ")
if not age.isdigit(): print("некорректные данные")
else:
    age = int(age)
    if age >= 18: print("вы совершеннолетний")
    else: print("вы несовершеннолетний")
