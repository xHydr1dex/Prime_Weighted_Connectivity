# solution_bf.py
import itertools
import math

def simulate_tournament(skills, k):
    n = len(skills)
    total_outcomes = 0
    player1_topk_count = 0
    median_sum = 0.0

    # Generate all possible outcomes as permutations of wins/losses
    # For n > 10 this will be infeasible (brute-force)
    outcomes = list(itertools.product([0, 1], repeat=n*(n-1)//2))

    # Precompute pair indices for matches
    matches = []
    for i in range(n):
        for j in range(i+1, n):
            matches.append((i,j))

    for outcome in outcomes:
        wins = [0]*n
        prob = 1.0
        for idx, (i,j) in enumerate(matches):
            si, sj = skills[i], skills[j]
            p_i_wins = si / (si + sj)
            if outcome[idx] == 1:
                wins[i] += 1
                prob *= p_i_wins
            else:
                wins[j] += 1
                prob *= 1 - p_i_wins

        # Get top k players
        ranked = sorted(range(n), key=lambda x: (-wins[x], -skills[x]))
        topk = ranked[:k]

        # Median among top k
        top_skills = sorted([skills[p] for p in topk])
        if k % 2 == 1:
            median = top_skills[k//2]
        else:
            median = (top_skills[k//2 - 1] + top_skills[k//2]) / 2.0

        median_sum += median * prob
        if 0 in topk:  # player 1 is in top k
            player1_topk_count += prob

        total_outcomes += prob

    expected_median = median_sum / total_outcomes
    player1_prob = player1_topk_count / total_outcomes
    return expected_median, player1_prob

# Example input
if __name__ == "__main__":
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))

    em, p1_prob = simulate_tournament(skills, k)
    print(f"{em:.6f}")
    print(f"{p1_prob:.6f}")
