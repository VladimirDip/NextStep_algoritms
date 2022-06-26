import collections

def counter(first: list, second: list):
    count = collections.Counter(second)

    answer = []
    for i in first:
        if count[i] > 0:
            answer.append(i)
            count[i] -= 1
    return answer


def main():
    len_first = int(input())
    len_second = int(input())

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    print(*counter(first, second))


if __name__ == '__main__':
    main()