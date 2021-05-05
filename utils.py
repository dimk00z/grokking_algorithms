from random import randint


def create_ordered_list(start: int = 0,
                        step: int = 1,
                        end: int = 100):
    return [number+1 for number in range(start, end, step)]


def create_random_list(max_value=100):
    return [randint(0, max_value) for random_value in range(max_value)]
