
VERSION = '1.1beta'


def print_game():
    print("GAME")


def print_version():
    version = '___' + VERSION + '___'
    print('Version:', version)


def get_hero_hp(_hero_name):
    if _hero_name == 'Alice':
        return 5
    elif _hero_name == 'Bob':
        return 10
    else:
        return 7


def print_hero(_hero_name, _hero_hp):
    print('Hero name:', _hero_name)
    print('Hero hp:', _hero_hp)


def receive_damage(_hero_hp):
    return _hero_hp - 1


def heal_hero(_hero_hp):
    return _hero_hp + 1


def is_game_active(_hero_hp):
    return _hero_hp > 0


print_game()
print_version()

hero_name = input('Input hero name: ')
hero_hp = get_hero_hp(hero_name)

while is_game_active(hero_hp):
    print('==========================')
    print_hero(hero_name, hero_hp)
    print('1) Damage')
    print('2) Heal')
    command = input('[1,2]: ')
    if command == '1':
        hero_hp = receive_damage(hero_hp)
    elif command == '2':
        hero_hp = heal_hero(hero_hp)

print('Game over')
