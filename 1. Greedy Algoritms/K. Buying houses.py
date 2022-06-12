def get_count_houses(money: int, cost_houses: list):
    sort_cost_houses = sorted(cost_houses)
    count_houses = 0
    for price in sort_cost_houses:
        if money >= price:
            count_houses += 1
            money = money - price
        else:
            return count_houses


def main():
    houses_and_money = list(map(int, input().split()))
    cost_houses = list(map(int, input().split()))
    print(get_count_houses(houses_and_money[1], cost_houses))


if __name__ == '__main__':
    main()