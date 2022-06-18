from string import ascii_lowercase

alphabet = []


def get_alphabet(letter: str, position=0):
    if ascii_lowercase[position] == letter:
        alphabet.append(ascii_lowercase[position])
        return alphabet
    alphabet.append(ascii_lowercase[position])
    return get_alphabet(letter, position + 1)


def main():
    letter = input()
    print(*get_alphabet(letter))


if __name__ == '__main__':
    main()
