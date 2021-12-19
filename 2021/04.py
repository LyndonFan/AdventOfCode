from typing import Tuple
import re


class Board:
    def __init__(self, board_string: str) -> None:
        print(board_string)
        self.board = [[int(x) for x in re.split(" +", row.strip())]
                      for row in board_string.split('\n')]
        self.board_dict = {self.board[x][y]: (
            x, y) for x in range(5) for y in range(5)}
        self.board_hits = [[False for _ in range(5)] for _ in range(5)]
        self.last_call = None
        print("-"*40)

    def __call__(self, n: int) -> None:
        self.last_call = n
        if n in self.board_dict:
            x, y = self.board_dict[n]
            self.board_hits[x][y] = True

    @property
    def check_bingo(self) -> Tuple[bool, int]:
        # s is sum of all unmarked numbers on board
        s = sum(self.board[x][y] for x in range(5)
                for y in range(5) if not self.board_hits[x][y])
        score = s * self.last_call
        for row in self.board_hits:
            if all(row):
                return (True, score)
        for col in zip(*self.board_hits):
            if all(col):
                return (True, score)
        return (False, 0)


def q4(data):
    data = data.split("\n\n")
    num_order, boards = data[0], data[1:]
    num_order = [int(x) for x in num_order.split(',')]
    print(boards)
    boards = [Board(x) for x in boards]
    has_won = [False for _ in boards]
    for n in num_order:
        for i, board in enumerate(boards):
            board(n)
            has_bingo, score = board.check_bingo
            if has_bingo:
                # return score # for part a
                has_won[i] = True
                if all(has_won):
                    return score


if __name__ == "__main__":
    with open("4.txt", "r") as f:
        data = f.read().strip()
    print(q4(data))
