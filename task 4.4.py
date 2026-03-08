
def decorator(func):
    def wrapper(*args, **kwargs):

        print(f"функция {func.__name__} вызвана с аргументами\n"
              f"позиционные: {args}\n"
              f"именованные: {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper
@decorator
def square(x,y):
    print(f"Площадь прямоугольника: {x * y}")

square(10,12)