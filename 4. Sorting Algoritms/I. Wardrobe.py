def clean_wardrobe(clothes: list):
    if len(clothes) > 1:
        mid = len(clothes) // 2
        left = clothes[:mid]
        right = clothes[mid:]
        clean_wardrobe(left)
        clean_wardrobe(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                clothes[k] = left[i]
                i += 1
            else:
                clothes[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            clothes[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            clothes[k] = right[j]
            j += 1
            k += 1
    return clothes


def main():
    len_array = int(input())
    clothes = [int(element) for element in input().split()]
    print(clean_wardrobe(clothes))


if __name__ == '__main__':
    main()
