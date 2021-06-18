def make_field():
    list_field = []
    for i in range(3):
        list_field.append(['*'] *3)
    return list_field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()

def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0]==field[i][1]==field[i][2]:
            return True
        if field[i][0] != '*' and field[0][i]==field[1][i]==field[2][i]:
            return True
    if field[0][0] != '*' and field[0][0]==field[1][1]==field[2][2]:
        return True
    if field[0][2] != '*' and field[0][2]==field[1][1]==field[2][0]:
        return True

def end_game(field):
    if win(field): 
        return True    
    
    for i in range(3):
        for j in range(3):
            if (field[i][j] == '*'):
                return False
    return True


def play():
    game_field = make_field();
    current_sumbol = 'X'

    while not end_game(game_field):
        print_field(game_field)

        while True:
            x, y = [int(x) for x in input('Введите координаты поля через пробел, куда хотите поставить {0} '.format(current_sumbol)).split(' ')]
            if (0>x>3 and 0>y>3):
                print('Координата не может быть больше 3 и меньше 0. Повторите ввод')
            elif (game_field[x-1][y-1] != '*'):
                print ('Клетка уже занята, введите другие координаты.')
            else:
                break
       
        game_field[x-1][y-1] = current_sumbol

        current_sumbol = 'O' if current_sumbol=='X' else 'X'


    if win(game_field):
        print('Поздравляю, {0}, вы победили!'.format('O' if current_sumbol=='X' else 'X') )
    else:
        print('Победила дружба!')

while True:
    play()
    continue_game = input('Начать новую игру? (y/n) ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        break