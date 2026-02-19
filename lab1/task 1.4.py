while True:
    num=input("введите целое число: ")
    if num=="exit": break
    elif num.lstrip('-').isdigit():
        print(f'цифр в этом числе: {len(num.lstrip('-'))}')
    else: print("введено не число")
