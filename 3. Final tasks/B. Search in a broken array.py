def get_index_element(search_of: int, array: list, left: int, right: int):

    if right >= left:
        middle = left + (right - left) // 2

        if array[middle] == search_of:
            return middle

        if array[middle] < array[right]:
            if array[middle] < search_of <= array[right]:
                return get_index_element(search_of, array, middle + 1, right)
            return get_index_element(search_of, array, left, middle - 1)

        if array[left] <= search_of < array[middle]:
            return get_index_element(search_of, array, left, middle - 1)
        return get_index_element(search_of, array, middle + 1, right)

    return -1


def main():
    len_array = int(input())
    search_of = int(input())
    array = list(map(int, input().split()))
    print(get_index_element(search_of, array, left=0, right=len_array-1))


if __name__ == '__main__':
    main( )