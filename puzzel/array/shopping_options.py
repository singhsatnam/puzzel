from typing import List


def shoppingOptions(pairOfJeans, pairOfShoes, pairOfSkirts, pairOfTops, dollars):
    dp = [0 for _ in range(dollars + 1)]  # you can trim this too, looking at max/min pairs, but unnecessary.
    count = 0

    for a in pairOfJeans:
        for b in pairOfShoes:
            if 0 <= a + b <= dollars:
                dp[a + b] += 1

    for i in range(1, dollars + 1):
        dp[i] += dp[i - 1]

    for c in pairOfSkirts:
        for d in pairOfTops:
            if 0 <= dollars - (c + d) <= dollars:
                count += dp[dollars - (c + d)]

    return count


print(shoppingOptions([2, 3], [4], [2, 3], [1, 2], 10))

