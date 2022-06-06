def collect_backpack(capacity, n):
    array = []
    for i in range(n):
        value, weight = input().split()
        array.append((int(value), int(weight), i))

    array.sort(key=lambda elem: (-elem[0], elem[1], elem[2]))

    result = []
    for item in range(n):
        item_weight = array[item][1]

        if item_weight <= capacity:
            capacity -= item_weight

            item_index = array[item][2]
            result.append(item_index)

    result.sort()
    return result


if __name__ == "__main__":
    print(*collect_backpack(int(input()), int(input())))