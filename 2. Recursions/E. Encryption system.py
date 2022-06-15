def get_factorial(number: int):
    if number < 2:
        return 1
    return get_factorial(number-1) * number


def main():
    number = int(input())
    print(get_factorial(number))


if __name__ == '__main__':
    main()