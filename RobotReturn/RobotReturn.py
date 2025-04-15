#!/usr/bin/env python3

def judgeCircle(moves: str) -> bool:
    start = [0, 0]
    validMoves = {
        "R" : [1, 0],
        "L" : [-1, 0],
        "U" : [0, 1],
        "D" : [0, -1]
    }

    for move in moves:
        print(validMoves[move])
        start[0] += validMoves[move][0]

        start[1] += validMoves[move][1]
    print(start)
    return start == [0, 0]


if __name__ == "__main__":
    move1 = "UD"
    move2 = "LLLL"
    print(judgeCircle(move1))
    print(judgeCircle(move2))