def insertion(array: list):
    for i, element in enumerate(array):
        revers = False
        min_index = i

        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                revers = True
                min_index = j

        if revers:
            array[i], array[min_index] = array[min_index], array[i]

    return array


def main():
    len_array = int(input())
    array = list(map(int, input().split()))
    print(insertion(array))


if __name__ == '__main__':
    main()