def make_happy_children(children_greed: list, cookies: list) -> int:
    children_cookies = zip(children_greed, cookies)
    happy_children = 0
    for pair in children_cookies:
        if pair[0] <= pair[1]:
            happy_children += 1
    return happy_children


def main():
    count_children = int(input())
    children_greed = list(map(int, input().split()))
    count_cookies = int(input())
    cookies = list(map(int, input().split()))
    print(make_happy_children(children_greed, cookies))


if __name__ == '__main__':
    main()