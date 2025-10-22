# Statistical Tournament

## Overview
This repository contains an original competitive programming problem titled **"Statistical Tournament"**. The problem involves probability, statistics, and expected outcomes in a tournament setting. Players have skill ratings, and match outcomes are probabilistic based on their relative skills.

The problem is designed for **Codeforces Div1/Div2 level** and includes:

- Problem statement
- Brute-force and optimal solutions
- Test cases
- Qwen AI evaluation attempts
- Test case generator

---

## Problem Summary
- **Players:** `n` players with skill ratings `S_i`.
- **Match Probability:** The probability that player `i` beats player `j` is:

\[
P(i \text{ beats } j) = \frac{S_i}{S_i + S_j}
\]

- **Tournament:** All players play matches, and the top `k` players advance.
- **Tasks:**
  1. Compute the expected skill of the **median player** among the top `k`.
  2. Compute the probability that **player 1 reaches the top `k`**.

- **Input:** 
  - Line 1: `n k` (1 ≤ k ≤ n ≤ 5000)
  - Line 2: `S_1 S_2 ... S_n` (1 ≤ S_i ≤ 10^6)

- **Output:**
  1. Expected skill of median player (6 decimal places)
  2. Probability of player 1 reaching top `k` (6 decimal places)

---

## Folder Structure

├── qwen/
│ ├── conversations.md # Qwen AI runs
│ ├── run_01.py
│ ├── run_02.py
│ └── run_03.py
├── test_cases/
│ ├── 1.in
│ ├── 1.out
│ └── ... (at least 5 cases)
├── idea.md # Problem idea and evolution
├── problem.md # Full problem statement
├── solution.md # Explanation of optimal solution
├── solution.py # Optimal Python solution
├── solution_bf.py # Brute-force Python solution
├── requirements.json # Time and memory limits
└── README.md # Project overview

---

## How to Run

1. **Optimal solution:**
python solution.py < test_cases/1.in

2. **Brute-force solution:**

python solution_bf.py < test_cases/1.in

Evaluation with Qwen AI

Three Qwen AI runs (run_01.py, run_02.py, run_03.py) are included under qwen/. The AI fails on all three plausible attempts, demonstrating problem difficulty and originality.

