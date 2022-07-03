def simple_number(number: int) -> bool:
    flag = False
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True


def get_count_simple_number(number: int) -> int:
    count_number = 0
    for n in range(number-1, 1, -1):
        if simple_number(n):
            count_number += 1

    return count_number


def main():
    number = int(input())
    print(get_count_simple_number(number))


if __name__ == '__main__':
    main()