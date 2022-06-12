def get_len_winning_array(array: list):
    array_winning = []
    last_big_winning_array = 0
    elem_of_array = 0

    for elem in array:
        if elem >= elem_of_array:
            elem_of_array = elem
            array_winning.append(elem)
        elif elem < elem_of_array:
            elem_of_array = elem
            count_winning = len(array_winning)
            if last_big_winning_array < count_winning:
                last_big_winning_array = count_winning
                array_winning.clear()
                array_winning.append(elem)

    return last_big_winning_array


def main():
    len_array = int(input())
    array = list(map(int, input().split()))
    print(get_len_winning_array(array))


if __name__ == '__main__':
    main()