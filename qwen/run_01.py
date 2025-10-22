from itertools import combinations

def solve_exact(n, k, skills):
    # Precompute win probabilities for every pair
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                P[i][j] = skills[i] / (skills[i] + skills[j])
    
    # List all matches (i, j) with i < j
    matches = []
    for i in range(n):
        for j in range(i + 1, n):
            matches.append((i, j))
    total_matches = len(matches)
    
    expected_median = 0.0
    prob_player0_in_topk = 0.0

    # Iterate over all 2^(#matches) possible outcomes
    for outcome in range(1 << total_matches):
        prob = 1.0
        wins = [0] * n

        # Simulate each match
        for idx, (i, j) in enumerate(matches):
            if outcome & (1 << idx):
                # i wins
                wins[i] += 1
                prob *= P[i][j]
            else:
                # j wins
                wins[j] += 1
                prob *= P[j][i]

        # Determine ranking: sort by wins (desc), then by index (asc) for tie-breaking
        players = list(range(n))
        players.sort(key=lambda x: (-wins[x], x))
        topk_players = players[:k]
        topk_skills = [skills[i] for i in topk_players]
        topk_skills.sort()

        # Compute median skill of top-k
        if k % 2 == 1:
            median_skill = topk_skills[k // 2]
        else:
            median_skill = (topk_skills[k // 2 - 1] + topk_skills[k // 2]) / 2.0

        expected_median += prob * median_skill
        if 0 in topk_players:
            prob_player0_in_topk += prob

    return expected_median, prob_player0_in_topk


# Run the three test cases
test_cases = [
    (4, 2, [1, 2, 3, 4]),
    (5, 3, [5, 1, 3, 4, 2]),
    (6, 4, [10, 20, 30, 40, 50, 60])
]

for n, k, skills in test_cases:
    med, prob0 = solve_exact(n, k, skills)
    print(f"{med:.6f}")
    print(f"{prob0:.6f}")
