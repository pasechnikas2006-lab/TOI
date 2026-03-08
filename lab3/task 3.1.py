list1=input("введите ваш список: ").split()
mlt=(input("введите множитель(2 по умолчанию): "))
if mlt=='': mlt=2
elif not mlt.isalpha(): mlt=int(mlt)
list2=[]
for item in list1:
    if not item.isalpha(): list2.append(float(item))
    else: list2.append(str(item))

def mult(lst: list, mlt: int)-> list:
    lst2=[]
    for item in lst:
        lst2.append(item*mlt)
    return lst2

result = map(lambda x:x*mlt , list2 )
print(f"обычная функция: {mult(list2, mlt)}")
print(f"лямбда функция: {list(result)}")

