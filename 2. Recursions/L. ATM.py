def get_money(need_money: int,count_coins: int, quality_coins: list):
    table = [0 for _ in range(need_money + 1)]
    table[0] = 1

    for i in range(0, count_coins):
        for j in range(quality_coins[i], need_money + 1):
            table[j] += table[j - quality_coins[i]]
    return table[need_money]


def main():
    need_money = int(input())
    count_coins = int(input())
    quality_coins = list(map(int, input().split()))
    print(get_money(need_money, count_coins, quality_coins))


if __name__ == '__main__':
    main()
