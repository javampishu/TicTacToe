cells = "         "
board = [[cells[6], cells[3], cells[0]],
         [cells[7], cells[4], cells[1]],
         [cells[8], cells[5], cells[2]]]

def print_cells():
    print(9 * '-')
    print(f"| {board[0][2]} {board[1][2]} {board[2][2]} |")
    print(f"| {board[0][1]} {board[1][1]} {board[2][1]} |")
    print(f"| {board[0][0]} {board[1][0]} {board[2][0]} |")
    print(9 * '-')

def check_move(elements):
    global result
    straights =[elements[:3], elements[3:6], elements[6:], elements[0:9:3], elements[1:9:3], elements[2:9:3], elements[0:9:4],
    elements[2:7:2]]

    if 'XXX' in straights:
        result = 'X wins'
    elif 'OOO' in straights:
        result = 'O wins'
    elif elements.count(' ') == 0:
        result = 'Draw'
    else:
        result = ''

def moves():
    global elements
    xx = 0
    yy = 0
    while True:
        next_move = input("Enter coordinates: ", ).split()

        if next_move[0].isdecimal() and next_move[1].isdecimal():
            if int(next_move[0]) > 3 or int(next_move[1]) > 3:
                print("Coordinates should be from 1 to 3!")
            elif board[int(next_move[0]) - 1][int(next_move[1]) - 1] in ("X", "O"):
                print("This cell is occupied! Choose another one!")
            else:
                elements = "".join(board[0]) + "".join(board[1]) + "".join(board[2])
                for i in elements:
                    if i == "X":
                        xx += 1;
                    elif i == "O":
                        yy += 1
                if xx <= yy:
                    board[int(next_move[0]) - 1][int(next_move[1]) - 1] = "X"
                else:
                    board[int(next_move[0]) - 1][int(next_move[1]) - 1] = "O"
                elements = "".join(board[0]) + "".join(board[1]) + "".join(board[2])
                print_cells()
                return elements
        else:
            print("You should enter numbers!")

print_cells()
while True:
    moves()
    check_move(elements)
    if len(result) > 0:
        print(result)
        break
    else:
        continue


