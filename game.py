import random 
def make_move(curr_state, player, other_player, max=True):
    #print(curr_state)
    available_moves = [i for i in range(0, 9) if curr_state[i]==' ']
    
    if win_state(curr_state, other_player):
        score = 0
        if not max:
            score = 1*(len(available_moves)+1)
        else:
            score = -1*(len(available_moves)+1)
        #print(curr_state, score)
        return curr_state, score

    if draw_state(available_moves):
        return curr_state,0
    if max:
        best= -100
    else:
        best = 100
    final_next_state =[]
    sc=-100
    #print(available_moves)
    curr = curr_state[:]
    for ind in available_moves:
        
        curr[ind] = player
        #print(curr, ind, player, not max, other_player)
        next_state, sc = make_move(curr, other_player, player, not max)
        
        if max and sc > best:
            best = sc
            final_next_state = curr[:]
        if not max and sc < best:
            best = sc
            final_next_state = curr[:]
        curr[ind]=' '
    return final_next_state, best

def draw_state(available_moves):
     return len(available_moves)==0
               

def win_state(curr_state, player):
    state = [player, player, player]
    #print(curr_state)
    if [curr_state[i] for i in range(0,3)] == state:
        return True
    elif [curr_state[i] for i in range(3,6)] == state:
        return True
    elif [curr_state[i] for i in range(6,9)] == state:
        return True
    elif [curr_state[i] for i in range(0,9,3)] == state:
        return True
    elif [curr_state[i] for i in range(1, 9, 3)] == state:
        return True
    elif [curr_state[i] for i in range(2,9,3)] == state:
        return True
    elif [curr_state[i] for i in range(0,9,4)] == state:
        return True
    elif [curr_state[2], curr_state[4], curr_state[6]]== state:
        return True
    else:
        i=1
    
    return False 
        
def print_state( curr_state, player=None) :
    sep = "--------------------"
    print(sep)
    for i in  range(0,9,3):
        row = "| " + " || ".join(curr_state[i:i+3]) + " | "
        print(row)
    print(sep)
    
def play_game():
    curr_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    curr_player =  'X'
    other_player = 'O'
    moves = 0
    available_moves=[]
    while not win_state(curr_state, other_player) :
        available_moves =  [i for i in range(0, 9) if curr_state[i]==' ']
        if draw_state(available_moves):
            break
        print_state(curr_state)
        moves = moves + 1
        if curr_player == 'O':
            print('Your turn')
            pos = input()
            while( pos>=9 or curr_state[pos] != ' '):
                print('Incorrent position; choose another position')
                pos = input()
            curr_state[pos] = curr_player
            
        else:
            print("Computer's Turn ")
            next_state, sc = make_move(curr_state, curr_player, other_player, True)
            curr_state = next_state
            #res = random.randrange(len(available_moves))
            #curr_state[available_moves[res]] = curr_player
        if curr_player == 'X':
            curr_player = 'O'
            other_player = 'X'
        else:
            curr_player = 'X'
            other_player = 'O'
    print("End State")
    print(print_state(curr_state))
    print("")
    if draw_state(available_moves):
        print("Game Drawn")
    else:
        print("Game Over : " + other_player + " Won " + "#Moves" + str(moves))

if __name__ == '__main__':
    curr_state = ['X','O','O',' ','O',' ',' ','X','X']
    #curr_state = ['X','O','O','X','O',' ','O','X','X']
    #curr_state = ['X', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'X']
    #next_state, score = make_move(curr_state, 'X', 'O', True)
    #print(print_state(curr_state))
    #print(next_state)
    #print(print_state(next_state))
    #print(score)
    play_game()