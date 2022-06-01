def scheduling(tuple_time: list):
    main_scheduling = []
    tuple_time = sorted(tuple_time)
    for lesson_number in range(len(tuple_time)):
        if len(main_scheduling) == 0:
            main_scheduling.append(tuple_time[lesson_number])

        last_lesson = main_scheduling[-1]

        if last_lesson[1] <= tuple_time[lesson_number][0]:
            main_scheduling.append(tuple_time[lesson_number])

    return main_scheduling


def main():
    counts_lessons = int(input())
    lessons = []

    for _ in range(counts_lessons):
        lessons_time = tuple(map(float, input().split()))
        lessons.append(lessons_time)

    schedule = scheduling(lessons)
    for row in schedule:
        print(*row)


if __name__ == '__main__':
    main()