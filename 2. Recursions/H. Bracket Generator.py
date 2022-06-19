def generate_bracket(count_bracket: int, co=0, cc=0, ans=''):
    if co + cc == 2 * count_bracket:
        print(ans)
        return
    if co < count_bracket:
        generate_bracket(count_bracket, co + 1, cc, ans+'(')
    if co > cc:
        generate_bracket(count_bracket, co, cc+1, ans+')')


def main():
    count_bracket = int(input())
    print(generate_bracket(count_bracket))


if __name__ == '__main__':
    main()