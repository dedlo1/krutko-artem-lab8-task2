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
    """

    def checking(row: str, numbers_out: str = "") -> str | None:
        """subfunc to run horizontal str"""
        for symb in row:
            if symb.isdigit():
                if symb in numbers_out:
                    return None
                numbers_out += symb
        return numbers_out

    def checking_two(i: int, numbers_out: str = "") -> str | None:
        """subfunc to run vertical str"""
        for row in board:
            if row[i].isdigit():
                if row[i] in numbers_out:
                    return None
                numbers_out += row[i]

            if checking(row) is None:
                return None
        return numbers_out

    for i in range(len(board[0])):
        if checking_two(i) is None:
            return False

    for i in range(5, len(board[0]) + 1):
        i = -i
        numbers = ""
        board_temp = []

        for index, row in enumerate(board):
            if -index == i:
                break
            board_temp.append(row[i:])

        for index in range(len(board[0])):
            check = checking_two(index, numbers)
            if check is None:
                return False
            numbers = check
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
