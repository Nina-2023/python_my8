class DivisionByZeroError(Exception):
    """Исключение деления на ноль"""
    pass

while True:
    try:
        numerator = int(input('Введите числитель: '))
        denominator = int(input('Введите знаменатель: '))
        if denominator == 0:
            raise DivisionByZeroError('На ноль делить нельзя!')
        result = numerator / denominator
    except ValueError:
        print('Вводите только целые числа!')
    except DivisionByZeroError as err:
        print(err)
    else:
        print(f'Результат деления: {result}')
        break