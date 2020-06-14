theBoard = {'1-L': '', '1-M': '', '1-R': '',
            '2-L': '', '2-M': '', '2-R': '',
            '3-L': '', '3-M': '', '3-R': ''}

theBoard['2-M'] = 'O'


def printBoard(board):
    print(board['1-L'] + '|' + board['1-M'] + '|' + board['1-R'])
    print('-----')
    print(board['2-L'] + '|' + board['2-M'] + '|' + board['2-R'])
    print('-----')
    print(board['3-L'] + '|' + board['3-M'] + '|' + board['3-R'])
