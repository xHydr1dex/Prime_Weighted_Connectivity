Problem Title: Statistical Tournament
Story / Flavor Text

The Global Gamers League (GGL) is hosting a revolutionary tournament called “The Statistical Gauntlet”, where strategy isn’t just about skill—it’s about probabilities and statistics.

In this tournament:

There are n elite players, each with a known skill rating S_i.

Matches are not deterministic; instead, they are probabilistic. If player i faces player j, the probability that i wins is:

𝑃
(
i beats j
)
=
𝑆
𝑖
𝑆
𝑖
+
𝑆
𝑗
P(i beats j)=
S
i
	​

+S
j
	​

S
i
	​

	​


The tournament proceeds in rounds where every player gets a chance to compete with others. After all matches, only the top k players advance to the next stage.

The GGL organizers want to extract key statistical insights:

What is the expected skill rating of the median player among the top k players?

What is the probability that the first player in the list reaches the top k?

You, as the official statistician, are tasked with computing these values efficiently, because the tournament software must provide live analytics during matches.

Input

First line: two integers n and k (1 ≤ k ≤ n ≤ 5000).

Second line: n integers S_1, S_2, ..., S_n (1 ≤ S_i ≤ 10^6), the skill ratings of the players.

Output

Line 1: Expected skill of the median player among the top k.

Line 2: Probability that player 1 reaches the top k.

Output values must have 6 decimal places of precision.

Constraints

There may be multiple players with the same skill rating.

The tournament outcomes are independent probabilistic events.

Median of the top k is defined as the middle value if k is odd or the average of the two middle values if k is even.

Example

Input

4 2
1 2 3 4


Output

3.500000
0.583333


Explanation

All possible match outcomes are considered with the given probability model.

Expected median among the top 2 players = 3.5.

Probability of player 1 reaching top 2 = 7/12 ≈ 0.583333.