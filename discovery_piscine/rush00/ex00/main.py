from checkmate import checkmate

def parse_board(board):
    """Turn the board string into a list of rows, or raise BoardError."""
    if not isinstance(board, str):
        print("error0")
        exit(1)
 
    rows = [line.strip() for line in board.strip().splitlines() if line.strip()]
    # print(rows)
    size = len(rows)
 
    if size == 0:
        print("error1")
        exit(1)
    if any(len(row) != size for row in rows):
        print("error2")
        exit(1)
 
    kings = sum(row.count('K') for row in rows)
    if kings != 1:
        print("error3")
        # print(kings)
        exit(1)
 
    return rows

def main():
    board = """\
....
.K..
....
....\

"""
    parse_board(board)
    checkmate(board)


if __name__ == "__main__":
    main()
