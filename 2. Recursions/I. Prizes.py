def get_answer(count_winners: int, coins: list, ):
    one_prize = sum(coins) / count_winners

    result_prize = 0
    i = 0
    while i < len(coins):
        coin = coins[i]
        i += 1
        if coin <= (one_prize - result_prize):
            result_prize += coin
            coins.pop(i-1)
            i = 0  
        if result_prize == one_prize:
            result_prize = 0
            count_winners -= 1
    return count_winners == 0


def main():
    count_winners = int(input())
    count_coins = int(input())
    coins = list(map(int, input().split()))
    print(get_answer(count_winners, coins))


if __name__ == '__main__':
    main()
