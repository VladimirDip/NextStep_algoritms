def get_perimetr(sides: list):
    sides.sort()
    for n in range(len(sides) - 1, 0, -1):
        perimeter = sides[n] < sides[n - 1] + sides[n - 2]
        if perimeter:
            perimeter = sides[n] + sides[n - 1] + sides[n - 2]
            return perimeter
    return


def main():
    len_array = int(input())
    sides = list(map(int, input().split()))
    print(get_perimetr(sides))


if __name__ == '__main__':
    main()
