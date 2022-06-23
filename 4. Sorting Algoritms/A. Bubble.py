def bubble(array: list, len_array: int):
    for _ in range(len_array):
        for n in range(len_array - 1):
            try:
                if array[n] > array[n + 1]:
                    array[n], array[n + 1] = array[n + 1], array[n]
            except:
                continue
    return array


def main():
    len_array = int(input())
    array = list(map(int, input().split()))
    print(bubble(array, len_array))


if __name__ == '__main__':
    main()
