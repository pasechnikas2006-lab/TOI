S = input("введите числа через пробел: ").split()
pwr =int(input("Введите степень(целое число): "))
lst1 = []
for i in S:
    if not i.isalpha():
        i=float(i)
        lst1.append(i**pwr)
    else: lst1.append(i*pwr)
print(lst1)
