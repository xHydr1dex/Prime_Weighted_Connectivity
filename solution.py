import sys
from itertools import combinations

def prob_first_in_top_k(skills, k):
    n = len(skills)
    p1 = skills[0]
    other = skills[1:]

    # dp[w] = probability that player 1 wins exactly w matches
    dp = [0.0] * (n)
    dp[0] = 1.0

    for s in other:
        next_dp = [0.0] * (n)
        for w in range(n-1):
            win = dp[w] * (p1 / (p1 + s))
            lose = dp[w] * (s / (p1 + s))
            next_dp[w+1] += win
            next_dp[w] += lose
        dp = next_dp

    # player 1 in top k if wins >= minimum required to be in top k
    top_prob = 0.0
    for wins in range(n):
        # Simple approximation: assume more wins -> top k
        if wins >= n - k:
            top_prob += dp[wins]

    return top_prob

def expected_median_top_k(skills, k):
    n = len(skills)
    skills_sorted = sorted(skills, reverse=True)
    
    # Approximate expected median using top k skills
    top_k_skills = skills_sorted[:k]
    top_k_skills.sort()
    
    if k % 2 == 1:
        median = top_k_skills[k//2]
    else:
        median = (top_k_skills[k//2 - 1] + top_k_skills[k//2]) / 2
    
    return median

# Read input
n, k = map(int, sys.stdin.readline().split())
skills = list(map(int, sys.stdin.readline().split()))

median = expected_median_top_k(skills, k)
prob_top_k = prob_first_in_top_k(skills, k)

print(f"{median:.6f}")
print(f"{prob_top_k:.6f}")
