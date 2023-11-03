""" Puzzle """


def validate_board(board: list[str]) -> bool:
    """ Checking if board is valid

    GitHub:
    https://github.com/dedlo1/krutko-artem-lab8-task2

    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 " 5   9   ",\
 " 6  83  *",\
 "3  3   **",\
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

    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "38     **",\
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
 "3  8   **",\
 "  8  2***",\
 "8 2  ****"\
])
    True
    """

    horizontal = [sorted([int(i) for i in row if i.isdigit()]) for row in board]
    vertical = [
        sorted([int(row[i]) for row in board if row[i].isdigit()])
        for i in range(len(board))
    ]
    tmp_board, count, count2 = [], 0, -1
    for cut in range(9, 4, -1):
        tmp_lst = [row[count] for row in board][:cut] + list(board[count2][count + 1 :])
        tmp_board.append(sorted([int(i) for i in tmp_lst if i.isdigit()]))
        count += 1
        count2 -= 1
    return all(len(set(i)) == len(i) for i in horizontal + vertical + tmp_board)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
