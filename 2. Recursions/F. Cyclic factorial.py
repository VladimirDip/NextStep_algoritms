def get_factorial(number: int):
    factorial = 1
    for step in range(1, number + 1):
        factorial *= step
    return factorial


def main():
    number = int(input())
    print(get_factorial(number))


if __name__ == '__main__':
    main()
