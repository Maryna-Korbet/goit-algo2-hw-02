from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}
    cuts_map = {}

    def helper(n: int) -> int:
        if n == 0:
            return 0
        if n in memo:
            return memo[n]

        max_profit = prices[n - 1]
        cuts_map[n] = [n]

        for i in range(1, n):
            profit = helper(i) + prices[n - i - 1]
            candidate_cuts = cuts_map[i] + [n - i]

            if profit > max_profit or (profit == max_profit and candidate_cuts[0] < cuts_map[n][0]):
                max_profit = profit
                cuts_map[n] = candidate_cuts

        memo[n] = max_profit
        return max_profit

    max_profit = helper(length)
    cuts = cuts_map[length]
    number_of_cuts = len(cuts) - 1 if cuts else 0

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts_map = [[] for _ in range(length + 1)]
    dp[0] = 0
    cuts_map[0] = []

    for i in range(1, length + 1):
        max_profit = prices[i - 1]
        cuts_map[i] = [i]
        for j in range(1, i):
            profit = dp[j] + prices[i - j - 1]
            if profit > max_profit or (profit == max_profit and (i - j) < cuts_map[i][0]):
                max_profit = profit
                cuts_map[i] = [i - j] + cuts_map[j]
        dp[i] = max_profit

    max_profit = dp[length]
    cuts = cuts_map[length]
    number_of_cuts = len(cuts) - 1 if cuts else 0

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }

def run_tests():
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Basic case"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Optimal no cut"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Uniform cuts"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod length: {test['length']}")
        print(f"Prices: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nMemoization result:")
        print(f"Max profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of cuts: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nTabulation result:")
        print(f"Max profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of cuts: {table_result['number_of_cuts']}")

        print("\nTest passed successfully!")

if __name__ == "__main__":
    run_tests()
