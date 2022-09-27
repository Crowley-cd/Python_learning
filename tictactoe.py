
def check(entered_list):
    count_X = 0
    count_O = 0
    status_x = False
    status_o = False


    for l in entered_list:
        a,b,c = l[0], l[1], l[2]
        if a == b and b == c and c == 'X':
            status_x = True
        if a == b and b == c and c == 'O':
            status_o = True

    if entered_list[0][0] == entered_list[1][0] == entered_list[2][0] == 'X':
        status_x = True
    if entered_list[0][0] == entered_list[1][0] == entered_list[2][0] == 'O':
        status_o = True
    if entered_list[0][1] == entered_list[1][1] == entered_list[2][1] == 'X':
        status_x = True
    if entered_list[0][1] == entered_list[1][1] == entered_list[2][1] == 'O':
        status_o = True
    if entered_list[0][2] == entered_list[1][2] == entered_list[2][2]== 'X':
        status_x = True
    if entered_list[0][2] == entered_list[1][2] == entered_list[2][2]== 'O':
        status_o = True

    if entered_list[0][0] == entered_list[1][1] == entered_list[2][2] == 'X' or \
            entered_list[0][2] == entered_list[1][1] == entered_list[2][0] == 'X':
        status_x = True
    if entered_list[0][0] == entered_list[1][1] == entered_list[2][2] == 'O' or\
            entered_list[0][2] == entered_list[1][1] == entered_list[2][0] == 'O':
        status_o = True
        #make conclusion of win scenario

    if status_x == True and status_o == True:
        return print('Impossible')
    elif status_x == True and status_o == False:
        print('X wins')
        exit(1)
    elif status_x == False and status_o == True:
        print('O wins')
        exit(1)

    if ' ' not in GRID[0] and ' ' not in GRID[1] and ' ' not in GRID[2]:
        print('Draw')
        exit(0)

    if status_x == False and status_o == False:
        prnt_step()


def grid(grid):
    global GRID
    GRID = grid
    if not isinstance(GRID,list):
        GRID = [grid[:3],
                grid[3:6],
                grid[6:]]

    l1 = ' '.join(GRID[0])
    l2 = ' '.join(GRID[1])
    l3 = ' '.join(GRID[2])

    print('---------')
    print('| ' + l1 + ' |')
    print('| ' + l2 + ' |')
    print('| ' + l3 + ' |')
    print('---------')

    check(GRID)


def inp():
    inpt = input()

    if len(inpt) != 9 or 'O' not in inpt and 'X' not in inpt and '_' not in inpt:
        return inp()
    grid(inpt)


def prnt_step():
    global GRID
    global STEP
    try:
        f_coord, s_coord = input().split()
        f_coord=int(f_coord)-1
        s_coord=int(s_coord)-1
        if GRID[f_coord][s_coord] == '_' or GRID[f_coord][s_coord] == ' ':
            if STEP % 2 == 0:
                GRID[f_coord] = list(GRID[f_coord])
                GRID[f_coord][s_coord] = 'X'
                GRID[f_coord] = ''.join(GRID[f_coord])
                STEP += 1
            else:
                GRID[f_coord] = list(GRID[f_coord])
                GRID[f_coord][s_coord] = 'O'
                GRID[f_coord] = ''.join(GRID[f_coord])
                STEP += 1
        else:
            print('This cell is occupied! Choose another one!')
            return prnt_step()
        grid(GRID)

    except (TypeError, ValueError):
        print('You should enter numbers!')
        return prnt_step()
    except LookupError:
        print('Coordinates should be from 1 to 3!')
        return prnt_step()


STEP = 0
GRID = '         '
grid(GRID)