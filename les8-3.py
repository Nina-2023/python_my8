class OnlyNumbersError(Exception):
    def __init__(self, text):
        self.txt = text

my_list = []

while True:
    user_input = input('Введите число: ')
    if user_input == 'stop':
        break
    try:
        number = int(user_input)
        my_list.append(number)
    except ValueError:
        print('Введено не число, попробуйте еще раз!')

print(f'Ваш список чисел: {my_list}')