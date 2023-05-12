"""
Задача №1. Соревнование по скорости печати

На соревновании по скорости печати нужно успеть за 15 секунд 9 раз написать код: f*5L9KuCfH(gXEnn
"""

from time import time


CODE = 'f*5L9KuCfH(gXEnn'


if __name__ == '__main__':
    start_t = time()
    for _ in range(9):
        if input('Enter code: ') != CODE:
            print('Неправильный пароль!')
            break
    else:
        if (run_time := time() - start_t) > 15:
            print(f'К сожалению вы не успели. Вы потратили {run_time:.2f} секунд')
        else:
            print('Поздравляем! Вы победили')
