def infinity_countdown(value):
    print(value)
    infinity_countdown(value-1)


def normal_countdown(value):
    print(value)
    if value == 0:
        return
    normal_countdown(value-1)


def main():
    # infinity_countdown(10)
    normal_countdown(10)


if __name__ == '__main__':
    main()
