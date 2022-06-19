def get_position(n_row: int, k_position: int, backet=None):
    if n_row == 1:
        return 0
    if k_position <= 2**(n_row - 1)/2:
        return get_position(n_row-1, k_position)
    else:
        return 1 - get_position(n_row - 1, k_position - 2**(n_row-1)/2)


def main():
    n_row = int(input())
    k_position = int(input())
    print(get_position(n_row, k_position))


if __name__ == '__main__':
    main()
