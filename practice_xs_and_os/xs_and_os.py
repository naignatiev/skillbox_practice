

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

is_finished = False

for i in range(9):
    # Выбираем кто сейчас играет
    if i % 2 == 0:
        player = 'X'
    else:
        player = '0'
    # Печатаем поле
    for j in range(3):
        print(f'|{field[j][0]}|{field[j][1]}|{field[j][2]}|')
    move_i, move_j = input('Ход: ').split(' ')
    field[int(move_i)][int(move_j)] = player

    for j in range(3):
        if field[0][j] == field[1][j] == field[2][j] == player or \
           field[j][0] == field[j][1] == field[j][2] == player or \
           field[0][0] == field[1][1] == field[2][2] == player or \
           field[0][2] == field[1][1] == field[2][0] == player:
            is_finished = True

    if is_finished:
        print(player, 'победили')
        break
else:
    print('Ничья')
