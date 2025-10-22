# Problem Title: Statistical Tournament

## Story / Flavor Text

The Global Gamers League (GGL) is hosting a revolutionary tournament called **“The Statistical Gauntlet”**, where strategy isn’t just about skill—it’s about probabilities and statistics.

In this tournament:

- There are \(n\) elite players, each with a known skill rating \(S_i\).
- Matches are **probabilistic**. If player \(i\) faces player \(j\), the probability that \(i\) wins is:

$$
P(i \text{ beats } j) = \frac{S_i}{S_i + S_j}
$$

- The tournament proceeds in rounds where every player gets a chance to compete with others. After all matches, only the top \(k\) players advance to the next stage.

The GGL organizers want to extract key statistical insights:

1. What is the expected skill rating of the **median player** among the top \(k\) players?
2. What is the probability that the **first player** in the list reaches the top \(k\)?

You, as the official statistician, are tasked with computing these values efficiently, because the tournament software must provide live analytics during matches.

---

## Input

- First line: two integers \(n\) and \(k\) (\(1 \le k \le n \le 5000\)).
- Second line: \(n\) integers \(S_1, S_2, \dots, S_n\) (\(1 \le S_i \le 10^6\)), the skill ratings of the players.

---

## Output

- **Line 1:** Expected skill of the median player among the top \(k\).  
- **Line 2:** Probability that player 1 reaches the top \(k\).  

> Output values must have **6 decimal places** of precision.

---

## Constraints

- There may be multiple players with the same skill rating.
- The tournament outcomes are **independent probabilistic events**.
- Median of the top \(k\) is defined as the middle value if \(k\) is odd, or the average of the two middle values if \(k\) is even.

---

## Example

### Input
