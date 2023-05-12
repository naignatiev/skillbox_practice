from string import ascii_letters
from random import choice, randint


def get_report_text():
    choice(ascii_letters)
    return '\n'.join([''.join([choice(ascii_letters) for _ in range(randint(40, 300))]) for _ in range(300)])


if __name__ == '__main__':
    for i in range(1, 5):
        with open(f'reports/report_{i}.txt', 'w') as f:
            f.write(get_report_text())
    print('Done')
