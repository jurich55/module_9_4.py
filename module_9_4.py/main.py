from random import choice
# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='UTF-8') as file:
            for tx_t in data_set:
                file.write(str(tx_t) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Может', 'Вниз')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
