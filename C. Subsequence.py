if __name__ == '__main__':
    subsequence = input()
    sequence = input()
    it = iter(sequence)
    print(all(letter in it for letter in subsequence))