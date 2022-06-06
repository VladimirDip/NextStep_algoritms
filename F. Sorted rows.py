import string


def sorted_rows(matrix_rows: list, len_rows: int) -> int:
    delete_column = 0
    alphabet = list(map(str, string.ascii_lowercase))
    for position_in_row in range(len_rows):
        last_position_letter = None
        for position_in_matrix in range(len(matrix_rows)):
            position_in_alphabet = alphabet.index(matrix_rows[position_in_matrix][position_in_row])
            if last_position_letter is None:
                last_position_letter = position_in_alphabet
            elif last_position_letter < position_in_alphabet:
                last_position_letter = position_in_alphabet
            else:
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

    # print(sorted_rows(matrix_rows, m_len))
    print(sorted_rows([['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']], 3))


if __name__ == '__main__':
    main()
