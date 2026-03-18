def simple_check(g: int):
    if g < 2:
        return False
    for i in range(2, g):
        if g % i == 0:
            return False
    return True

def generator():
    n = 2
    while True:
        if simple_check(n):
            yield n
        n += 1

def main():
    num =int(input())
    gen = generator()
    for i in range(num+1):
        print(next(gen))
main()
