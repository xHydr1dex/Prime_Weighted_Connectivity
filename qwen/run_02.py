from itertools import combinations

def main():
    test_cases = [
        (4, 2, [1, 2, 3, 4]),
        (5, 3, [5, 1, 3, 4, 2]),
        (6, 4, [10, 20, 30, 40, 50, 60])
    ]
    
    for n, k, skills in test_cases:
        # Precompute match list
        matches = [(i, j) for i in range(n) for j in range(i+1, n)]
        total = len(matches)
        exp_median = 0.0
        prob_p0 = 0.0

        # Iterate over all 2^total outcomes
        for mask in range(1 << total):
            wins = [0] * n
            prob = 1.0

            for idx, (i, j) in enumerate(matches):
                if mask & (1 << idx):
                    # i wins
                    wins[i] += 1
                    prob *= skills[i] / (skills[i] + skills[j])
                else:
                    # j wins
                    wins[j] += 1
                    prob *= skills[j] / (skills[i] + skills[j])

            # Rank players: more wins first, then lower index first
            ranked = sorted(range(n), key=lambda x: (-wins[x], x))
            topk = ranked[:k]
            topk_skills = [skills[i] for i in topk]
            topk_skills.sort()

            # Median
            if k % 2 == 1:
                median_val = topk_skills[k//2]
            else:
                median_val = (topk_skills[k//2 - 1] + topk_skills[k//2]) / 2.0

            exp_median += prob * median_val
            if 0 in topk:
                prob_p0 += prob

        print(f"{exp_median:.6f}")
        print(f"{prob_p0:.6f}")

if __name__ == "__main__":
    main()
    
