def simple_check(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

strt = int(input())
list1 = list(range(strt+1))

list2 = [ x for x in list1 if simple_check(x)==True ]
print(list2)
