#!/usr/bin/env python3

def judgeCircle(moves: str) -> bool:
    if moves.count('U') != moves.count('D') or moves.count('L') != moves.count('R'):
        return False
    return True


if __name__ == "__main__":
    move1 = "UD"
    move2 = "LLLL"
    print(judgeCircle(move1))
    print(judgeCircle(move2))