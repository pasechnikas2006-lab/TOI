import random
import json
import string


def generate_user_data():
    """
    Генерирует случайные данные пользователя и сохраняет в JSON файл
    """
    # Списки для генерации имен и email доменов
    first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emma",
                   "Alex", "Maria", "James", "Linda"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson",
                  "Miller", "Moore", "Taylor", "Anderson", "Thomas"]
    email_domains = ["example.com", "email.com", "mail.com", "web.com", "test.com"]

    # Генерируем имя
    name = f"{random.choice(first_names)} {random.choice(last_names)}"

    # Генерируем возраст (от 18 до 80)
    age = random.randint(18, 80)

    # Генерируем email
    email = f"{name.lower().replace(' ', '.')}.{random.randint(1, 999)}@{random.choice(email_domains)}"

    # Генерируем пароль (12 символов: буквы, цифры, знаки препинания)
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_chars, k=12))

    # Создаем словарь с данными пользователя
    user_data = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

    # Сохраняем в JSON файл
    with open("user_data.json", "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4, ensure_ascii=False)

    # Читаем JSON файл и выводим на экран
    with open("user_data.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

    return user_data


generate_user_data()
