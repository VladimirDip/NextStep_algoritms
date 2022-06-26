def get_bad_cockroach(first, second):
    intersection = set(first) & set(second)

    data = []
    for element in first:
        if element in intersection and element not in data:
            data.append(element)
    return data


def main():
    len_first = int(input())
    len_second = int(input())
    first = [int(element) for element in input().split()]
    second = [int(element) for element in input().split()]
    print(*get_bad_cockroach(first, second))


if __name__ == '__main__':
    main()
