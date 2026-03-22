import random
import string
from pathlib import Path


def create_random_files(directory):
    # Создаем директорию, если её не существует
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)

    created_files = []

    for _ in range(10):
        # Генерируем случайное имя файла из 8 символов (буквы и цифры)
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        filename += '.txt'

        # Создаем полный путь к файлу
        file_path = dir_path / filename

        # Создаем пустой файл
        file_path.touch()

        created_files.append(file_path)

    # Выводим абсолютные пути всех созданных файлов
    for file_path in created_files:
        print(file_path.absolute())


create_random_files("./random_files")
