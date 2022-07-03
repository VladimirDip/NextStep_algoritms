def get_lucky_ticket(number: str) -> bool:
    list_number = [int(x) for x in number]
    ticket = 0
    for n in list_number:
        ticket += n ** 2
    if ticket == 1:
        return True
    try:
        return get_lucky_ticket(str(ticket))
    except:
        return False


def main():
    number = input()
    print(get_lucky_ticket(number))


if __name__ == '__main__':
    main()
