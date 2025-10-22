from collections import defaultdict

def solve_with_random_tiebreak(n, k, skills):
    matches = [(i, j) for i in range(n) for j in range(i+1, n)]
    total_matches = len(matches)
    exp_median = 0.0
    prob_p0 = 0.0

    for mask in range(1 << total_matches):
        wins = [0] * n
        prob_outcome = 1.0

        for idx, (i, j) in enumerate(matches):
            if mask & (1 << idx):
                wins[i] += 1
                prob_outcome *= skills[i] / (skills[i] + skills[j])
            else:
                wins[j] += 1
                prob_outcome *= skills[j] / (skills[i] + skills[j])

        # Group players by win count
        win_to_players = defaultdict(list)
        for i in range(n):
            win_to_players[wins[i]].append(i)
        
        # Sort win counts descending
        sorted_wins = sorted(win_to_players.keys(), reverse=True)
        
        selected = []
        remaining = k
        for w in sorted_wins:
            group = win_to_players[w]
            if len(group) <= remaining:
                selected.extend(group)
                remaining -= len(group)
            else:
                # Tie at cutoff: choose 'remaining' players uniformly at random
                # We'll compute expected contribution
                t = len(group)
                need = remaining
                # Probability player i in group is selected = need / t
                # For median: we must average over all C(t, need) subsets
                # But for small t (≤6), we can enumerate subsets
                from itertools import combinations
                total_subsets = 0
                sum_median = 0.0
                sum_prob_p0 = 0.0

                for subset in combinations(group, need):
                    full_topk = selected + list(subset)
                    # Get skills of top-k
                    topk_skills = [skills[i] for i in full_topk]
                    topk_skills.sort()
                    if k % 2 == 1:
                        median_val = topk_skills[k//2]
                    else:
                        median_val = (topk_skills[k//2 - 1] + topk_skills[k//2]) / 2.0
                    sum_median += median_val
                    if 0 in full_topk:
                        sum_prob_p0 += 1
                    total_subsets += 1

                # Expected median contribution from this outcome
                exp_median += prob_outcome * (sum_median / total_subsets)
                prob_p0 += prob_outcome * (sum_prob_p0 / total_subsets)
                remaining = 0
                break

        if remaining > 0:
            # Should not happen, but just in case
            full_topk = selected
            topk_skills = [skills[i] for i in full_topk]
            topk_skills.sort()
            if k % 2 == 1:
                median_val = topk_skills[k//2]
            else:
                median_val = (topk_skills[k//2 - 1] + topk_skills[k//2]) / 2.0
            exp_median += prob_outcome * median_val
            if 0 in full_topk:
                prob_p0 += prob_outcome

    return exp_median, prob_p0


# Run test cases
test_cases = [
    (4, 2, [1, 2, 3, 4]),
    (5, 3, [5, 1, 3, 4, 2]),
    (6, 4, [10, 20, 30, 40, 50, 60])
]

for n, k, skills in test_cases:
    med, prob0 = solve_with_random_tiebreak(n, k, skills)
    print(f"{med:.6f}")
    print(f"{prob0:.6f}")

