import string


def sorted_rows(matrix_rows: list, len_rows: int, count: int) -> int:
    delete_column = 0
    alphabet = list(map(str, string.ascii_lowercase))
    for position_in_row in range(len_rows):
        for position_in_matrix in range(1, count):
            if matrix_rows[position_in_matrix][position_in_row] < matrix_rows[position_in_matrix - 1][position_in_row]:
                delete_column += 1
                continue
    return delete_column


def main():
    # n_count = int(input())
    # m_len = int(input())
    # matrix_rows = []
    # for _ in range(n_count):
    #     row = list(map(str, input()))
    #     matrix_rows.append(row)

    # print(sorted_rows(matrix_rows, m_len, n_count))
    print(sorted_rows([['c', 'b', 'a'], ['d', 'a', 'f'], ['a', 'a', 'a']], 3, 3))


if __name__ == '__main__':
    main()
