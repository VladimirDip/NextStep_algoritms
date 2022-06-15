def get_last_digit(number_fib: int, a=1, b=1):
    if number_fib < 3:
        return b
    return get_last_digit(number_fib - 1, a=b, b=(a + b) % 10)


def main():
    number_fib = int(input())
    print(get_last_digit(number_fib + 1))


if __name__ == '__main__':
    main()
