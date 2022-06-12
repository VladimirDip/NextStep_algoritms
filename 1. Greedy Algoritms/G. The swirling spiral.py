def spiral(spiral_matrix: list, rows: int, columns: int):
    dx, dy = 0, 1
    x, y = 0, 0

    for _ in range(rows * columns):
        print(spiral_matrix[x][y])
        spiral_matrix[x][y] = None
        nx, ny = x+dx, y+dy
        if 0 <= nx < rows and 0 <= ny < columns and spiral_matrix[nx][ny] is not None:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x+dx, y+dy


def main():
    # count_row = int(input())
    # count_column = int(input())
    # spiral_matrix = []
    # for _ in range(count_row):
    #     spiral_matrix.append(list(map(int, input().split())))

    print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 3, 4))


if __name__ == '__main__':
    main()
