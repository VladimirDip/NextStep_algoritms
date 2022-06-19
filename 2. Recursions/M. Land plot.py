def get_lenland(side_max: int, side_min: int):
    if side_max % side_min == 0:
        return side_min
    nod = side_max % side_min
    return get_lenland(side_max=side_min, side_min=nod)


def main():
    width = int(input())
    length = int(input())
    side_max = max(width, length)
    side_min = min(width, length)
    print(get_lenland(side_max, side_min))


if __name__ == '__main__':
    main()