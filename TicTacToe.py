#TicTacToe.py
import time

def print_board(values):
    print("\n")
    print("     |     |")
    time.sleep(0.2)
    print(f"  {values[0]}  |  {values[1]}  |  {values[2]}")
    print('_____|_____|_____')
    print("     |     |")
    time.sleep(0.2)
    print(f"  {values[3]}  |  {values[4]}  |  {values[5]}")
    print('_____|_____|_____')
    print("     |     |")
    time.sleep(0.2)
    print(f"  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("     |     |")
    print('\n')


def win_check(values,player_name):
    if values[1]==values[2]==values[3] or values[4]==values[5]==values[6] or values[7]==values[8]==values[9] or values[1]==values[4]==values[7] or values[2]==values[5]==values[8] or values[3]==values[6]==values[9] or  values[1]==values[5]==values[9] or values[3]==values[5]==values[7]:
        return True


def draw_check(moves):
    if ' ' not in values:
        return True



def play(player_name,symbol,moves):
    global values
    print(f"\n{player_name} It\'s your play")
    val = int(input(f"where you want put '{symbol}' between (1-9):"))
    values[val-1] = symbol
    print('\n')
    print_board(values)
    print('\n')
    
    if win_check(values,player_name)==True:
        print(f'{player_name.upper()} WIN!')
        print('\n')
        return 'win'
    elif moves==9:
        if draw_check(moves)==True:
            print('Match draw Try again!')
            return 'draw'
    return True
#start           
values = [i for i in range(1,10)]
print_board(values)
player1_name = input('enter your name :')
player2_name = input('enter your name :')
current_player = player2_name
moves = 0
while True:
    moves += 1
    if current_player == player1_name:
        current_player = player2_name
        if play(current_player,'X',moves)==True:
            continue
        else:
            break
    else:
        current_player = player1_name
        if play(current_player,'O',moves)== True:    
            continue
        else:
            break
