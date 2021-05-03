def infinity_countdown(value):
    print(value)
    infinity_countdown(value-1)


def normal_countdown(value):
    # print(value)
    if value == 0:
        return
    normal_countdown(value-1)


def simple_factorial(value):
    return 1 if value == 1 else value*simple_factorial(value-1)


def reverse_string(string):
    return '' if string == '' else reverse_string(string[1:])+string[0]


def main():
    # infinity_countdown(10)
    normal_countdown(5)
    print(simple_factorial(3))
    print(reverse_string('cat'))


if __name__ == '__main__':
    main()
