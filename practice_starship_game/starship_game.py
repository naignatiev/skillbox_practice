# Задание
# Написать игру, где корабль собирает звёздочки
# Игровое поле должно выглядеть так:
# SCORE:2
#  *
#      *
#    *
# | |W| |
from random import randint


# Наше стартовое меню
print('1) Начать игру')
print('2) Выйти')

command = int(input())
# Запускаем игру, если пользователь ввёл 1
if command == 1:
    # Инициализируем переменные необходимые для игры
    # Количество набранных очков
    score = 0
    # Позиция корабля
    # Все позиции кодируются одним числом 0 - слева, 1 - центр, 2 - право
    ship_pos = 1
    # Позиции звёздочек
    # Дальнее поле
    star_1_pos = randint(0, 2)
    # Среднее поле
    star_2_pos = randint(0, 2)
    # Ближайшее поле
    star_3_pos = randint(0, 2)
    # Запускаем бесконечный цикл игрового процесса
    while True:
        # ПЕРВАЯ СТАДИЯ: ВЫВОД ИГРОВОГО ПОЛЯ

        # Выводим строку с количеством очков.
        # Чтобы подавить пробел между сущностями меняем разделитель (sep) на пустую строку
        print('SCORE:', score, sep='')
        # Рисуем поля со звёздочками
        print(' ' + '  ' * star_1_pos + '*')
        print(' ' + '  ' * star_2_pos + '*')
        print(' ' + '  ' * star_3_pos + '*')
        # Рисуем поле корабля
        ship_row = '|'
        if ship_pos == 0:
            ship_row += 'W|'
        else:
            ship_row += ' |'
        if ship_pos == 1:
            ship_row += 'W|'
        else:
            ship_row += ' |'
        if ship_pos == 2:
            ship_row += 'W|'
        else:
            ship_row += ' |'
        print(ship_row)
        # ВТОРАЯ СТАДИЯ: ОБРАБОТКА КОМАНДЫ ПОЛЬЗОВАТЕЛЯ
        command = input()
        # Движение влево
        if command == 'L' and ship_pos > 0:
            ship_pos -= 1
        if command == 'R' and ship_pos < 2:
            ship_pos += 1
        # ТРЕТЬЯ СТАДИЯ: ДВИЖЕНИЕ ЗВЁЗД И НАКОПЛЕНИЕ ОЧКОВ
        # Накопление очков
        if star_3_pos == ship_pos:
            score += 1
        # Движение звёзд
        star_3_pos = star_2_pos
        star_2_pos = star_1_pos
        star_1_pos = randint(0, 2)

        if score == 5:
            print('Вы выиграли!')
            command = input('Хотите продолжить игру? [y/n]: ')
            if command == 'n':
                break


# Иначе ничего не делаем. Программа завершается
