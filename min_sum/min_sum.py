# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Calculate the sum of absolute values of elements in A. This represents the maximum possible sum we can achieve.
    sum_positive = sum(abs(a) for a in A)

    # Initialize a dynamic programming (DP) array to track which sums can be achieved. The length is sum_positive + 1 to include 0.
    dp = [0] * (sum_positive + 1)

    # The base case: a sum of 0 is always achievable.
    dp[0] = 1
    
    # Iterate over each element in array A.
    for a in A:
        # Take the absolute value of the current element. We consider absolute values because we can flip signs using the sequence S.
        a = abs(a)
        # Iterate backwards from sum_positive to a. This prevents double counting elements in our DP approach.
        for j in range(sum_positive, a - 1, -1):
            # If we can achieve a sum of j - a, then we can also achieve a sum of j by adding a.
            if dp[j - a]:
                dp[j] = 1 
    # Initialize the result to the maximum possible sum.
    result = sum_positive
            
    for i in range(sum_positive // 2 + 1):
        # If a sum of i is achievable, calculate the corresponding val(A, S) and update the result if it's smaller.
        if dp[i]:
            result = min(result, sum_positive - 2 * i)
            
    # Return the minimum val(A, S) found.
    return result