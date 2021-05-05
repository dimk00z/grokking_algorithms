
def create_ordered_list(start: int = 0,
                        step: int = 1,
                        end: int = 100):
    return [number+1 for number in range(start, end, step)]


def infinity_countdown(value):
    print(value)
    infinity_countdown(value-1)


def normal_countdown(value):
    if value == 0:
        return
    normal_countdown(value-1)


def simple_factorial(value):
    return 1 if value == 1 else value*simple_factorial(value-1)


def reverse_string(string):
    return '' if string == '' else reverse_string(string[1:])+string[0]


def recursive_sum(array):
    print(array)
    return 0 if not array else array[0] + recursive_sum(array[1:])


def main():
    # infinity_countdown(10)
    normal_countdown(5)
    print(simple_factorial(39))
    print(reverse_string('cat'))
    print(recursive_sum(create_ordered_list(end=10)))


if __name__ == '__main__':
    main()
