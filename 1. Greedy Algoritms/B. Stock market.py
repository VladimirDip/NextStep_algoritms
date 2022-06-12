def take_profit(n, prices):
    profit = 0
    for i in range(n - 1):
        today_price = prices[i]
        tomorrow_price = prices[i + 1]

        if tomorrow_price > today_price:
            profit += tomorrow_price - today_price

    return profit


if __name__ == '__main__':
    print(take_profit(int(input()), list(map(int, (input().split())))))