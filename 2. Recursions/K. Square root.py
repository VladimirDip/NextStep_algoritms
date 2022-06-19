def get_sqrt(number: int):
    if number < 0:
        return
    else:
        return round(number**0.5, 5)


def main():
    number = int(input())
    print(get_sqrt(number))


if __name__ == '__main__':
    main()