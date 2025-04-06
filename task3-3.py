def function_name(
    search: str,
    status: bool,
    *args: 'any',
    **kwargs: 'any'
) -> 'list[int] or str':
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search (str): Режим обработки. Допустимые значения: "args" или "kwargs".
        status (bool): Флаг, изменяющий поведение для режима "args".
        *args (any): Произвольные позиционные аргументы для режима "args".
        **kwargs (any): Произвольные именованные аргументы для режима "kwargs".

    Возвращает:
        list[int] or str:
            - Для search="args" и status=True: список целых чисел из args
            - Для search="args" и status=False: строку с объединёнными args
            - Для search="kwargs": строку с отформатированными ключами и значениями

    Вызывает:
        ValueError: Если параметр search имеет недопустимое значение
    """
    result: list[int] = []
    result_2: str = ""
    
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