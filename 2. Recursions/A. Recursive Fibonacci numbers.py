def get_number_fibonacci(position_number: int, a=1, b=1):
    if position_number < 3:
        return b
    return get_number_fibonacci(position_number - 1, a=b, b=(a+b))


def main():
    position_number = int(input())
    print(get_number_fibonacci(position_number + 1))
    

if __name__ == '__main__':
    main()
