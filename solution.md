# Idea for Statistical Tournament Problem

## Core Idea

The tournament is probabilistic: if player i faces player j, the probability that i wins is:

P(i beats j) = Si / (Si + Sj)

We are tasked with:
1. Computing the expected skill of the median player among the top k.
2. Computing the probability that player 1 reaches the top k.

## Approach

1. **Modeling the Probabilities**:
   - Each match is independent.
   - We can compute the probability distribution of players’ wins using dynamic programming or combinatorial reasoning.

2. **Top k Selection**:
   - For the probability of player 1 reaching top k:
     - Consider all win/loss outcomes.
     - Use DP to accumulate probabilities that player 1 has enough wins to be in top k.

3. **Expected Median**:
   - Use a probabilistic simulation or DP approach to compute the expected skill of the median of top k players.
   - Since the tournament outcomes are independent, this can be computed efficiently by considering all players’ probabilities to be in top k and their order statistics.

## Optimizations

- Avoid simulating all 2^(n*(n-1)/2) match outcomes directly.
- Use memoization for repeated subproblems in probability calculations.
- Leverage sorting and cumulative probability arrays to compute expected median efficiently.
