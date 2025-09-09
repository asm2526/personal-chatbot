"""
Edit distance (Levenshtein algorithm)
Computes the minimum number of edits (insert, delete, and substitute)
needed to transform one string into another
"""

def edit_distance(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)

    # initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # base cases
    for i in range(n+1):
        dp[i][0] = i # cost = deletions
    for j in range(m + 1):
        dp[0][j] = j # cost = insertions

    # fill DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i - 1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j], # deletion
                    dp[i][j-1], # insertion
                    dp[i-1][j-1] # substitution
                )
    
    return dp[n][m]