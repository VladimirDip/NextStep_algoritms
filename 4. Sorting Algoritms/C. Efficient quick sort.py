def quick_f(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_f(less) + [pivot] + quick_f(greater)


def main():
    array = list(map(int, input().split()))
    print(quick_f(array))


if __name__ == '__main__':
    main()
