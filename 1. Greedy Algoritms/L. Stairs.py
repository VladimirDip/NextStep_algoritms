def main():
    need_steps = {i for i in range(1, n)}
    for index, value in enumerate(stairs):
        available_steps = set(i + index for i in range(1, value + 1))
        need_steps.difference_update(available_steps)

    if not need_steps:
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    stairs = list(map(int, input().split()))
    print(main())