from typing import Union, List

def multiply_elements(
    elements: List[Union[int, float]], 
    multiplier: Union[int, float] = 2
) -> List[Union[int, float]]:
    return [x * multiplier for x in elements]

input_values = input("Введите список чисел через пробел: ").split()
numbers = [float(x) if '.' in x else int(x) for x in input_values]

multiplier_input = input("Введите множитель (по умолчанию 2): ")
multiplier = float(multiplier_input) if multiplier_input else 2

lambda_multiply = lambda lst, m: list(map(lambda x: x * m, lst))

print("Результат (функция):", multiply_elements(numbers, multiplier))
print("Результат (лямбда):", lambda_multiply(numbers, multiplier))