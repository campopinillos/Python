#!/usr/bin/env python3
"TIC TAC TOC GAME"

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
players = {'X': ' ', 'O': ' '}


def instruction():
    """Function that prints a board with the instructions"""
    print("press the numbers to place your position\n")
    print('  ', '1', '  |', '  ', '2', '  |', '  ', '3')
    print('-------+--------+--------')
    print('  ', '4', '  |', '  ', '5', '  |', '  ', '6')
    print('-------+--------+--------')
    print('  ', '7', '  |', '  ', '8', '  |', '  ', '9')
    print('=========================\n')


def check_winner(theBoard):
    """Function that checks if there is a winner"""
    check = 0
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        check = 1
    elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
        check = 1
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
        check = 1
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        check = 1
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        check = 1
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        check = 1
    elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
        check = 1
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        check = 1
    return check


def printBoard(theBoard):
    """Function that prints the board each trun"""
    print('  ', theBoard['1'], '  |', '  ',
          theBoard['2'], '  |', '  ', theBoard['3'])
    print('-------+--------+--------')
    print('  ', theBoard['4'], '  |', '  ',
          theBoard['5'], '  |', '  ', theBoard['6'])
    print('-------+--------+--------')
    print('  ', theBoard['7'], '  |', '  ',
          theBoard['8'], '  |', '  ', theBoard['9'], '\n')


def reset(theBoard):
    """Function that cleans the board to start again"""
    for k in theBoard.keys():
        theBoard[k] = ' '


def play(theBoard=theBoard, players=players):
    """Function to play"""
    node = "X"
    if players['X'] == ' ':
        print('Please enter the name of the player X')
        players['X'] = input()
    if players['O'] == ' ':
        print('Please enter the name of the player 0')
        players['O'] = input()
    print('\n\n{}\'s turn. Put your {}'.format(players[node], node))
    for i in range(9):
        instruction()
        printBoard(theBoard)
        print('it is {}\'s turn to play. Place your {}\n'.format(
            players[node], node))
        turn = input()
        while True:
            try:
                if theBoard[turn] == ' ':
                    theBoard[turn] = node
                    break
                else:
                    print("You've already played that move, place your",
                          node, "elsewhere\n")
                    instruction()
                    printBoard(theBoard)
                    turn = input()
            except KeyError:
                print('Please enter a valid number between 1 and 9')
                instruction()
                printBoard(theBoard)
                turn = input()

        check = check_winner(theBoard)
        if check == 1:
            printBoard(theBoard)
            print('The WINNER is ' + players[node].upper() + '\n')
            print('Do you play again?')
            answer = input('y / n: ').lower()
            if answer == 'y':
                reset(theBoard)
                play(theBoard, players)
            else:
                break
        else:
            node = 'O' if node == 'X' else 'X'
            i += 1
        if i == 10:
            print("No winner")
            print('Do you play again?')
            answer = input('y / n: ').lower()
            if answer == 'y':
                reset(theBoard)
                play(theBoard, players)
            else:
                break


if __name__ == "__main__":
    play(theBoard, players)
