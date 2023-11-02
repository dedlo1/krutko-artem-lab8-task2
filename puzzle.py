''' Puzzle '''

def validate_board(board: list[str])-> bool:
    ''' Checking board if it valid 
    
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 " 5   9 5 ",\
 " 6  83  *",\
 "3      **",\
 "  8  2***",\
 "  2  ****"\
])
    False

    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False
    '''

    for row in board:
        numbers = ''
        for symb in row:
            if symb.isdigit():
                if symb in numbers:
                    return False
                numbers += symb

    for i in range(len(board[0])):
        numbers = ''
        for row in board:
            if row[i].isdigit():
                if row[i] in numbers:
                    return False
                numbers += row[i]
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
