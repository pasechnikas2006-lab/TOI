
def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list[int] | str:
    """
    Обрабатывает аргументы в зависимости от параметров.

    аргументы:
        search: Режим ("args" или "kwargs")
        status: режим обработки (True - собирает все аргументы типа int в result, False - собирает все аргументы в result2)
        *args: Позиционные аргументы
        **kwargs: Именованные аргументы

    возвращает:
        List[int] - если search="args" и status=True
        str - в остальных случаях

    выводит ValueError если search не "args" и не "kwargs"
    """
    result: list = []
    result_2 : str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")