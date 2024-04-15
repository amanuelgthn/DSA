#!/usr/bin/python3
#!/usr/bin/python3

def solution(A):
    # Implement your solution here
    repeated = 0
    for i in A:
        # print("i", i, "repeated", repeated)
        repeated = repeated ^ i
        # print("affected", "repeated", repeated)
    return(repeated)

print(solution([9, 3, 9, 3, 5, 7, 5]))
