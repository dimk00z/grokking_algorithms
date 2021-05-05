from typing import List
from random import randint
from utils import create_random_list


def quicksort(unsorted_list: List[int]):

    if len(unsorted_list) < 2:
        return unsorted_list
    pivot_position = randint(0, len(unsorted_list)-1)

    pivot = unsorted_list[pivot_position]

    left_list = [value for position, value in enumerate(
        unsorted_list) if (value <= unsorted_list[pivot_position])
        and (position != pivot_position)]

    right_list = [value for position, value in enumerate(
        unsorted_list) if (value > unsorted_list[pivot_position])
        and (position != pivot_position)]

    return quicksort(left_list)+[pivot]+quicksort(right_list)


def main():
    unsorted_list = create_random_list(max_value=9)
    print(unsorted_list)
    sorted_list = quicksort(unsorted_list)
    print(sorted_list, len(sorted_list))


if __name__ == "__main__":
    main()
