from typing import List


def create_ordered_list(start: int = 0,
                        step: int = 1,
                        end: int = 100):
    return [number+1 for number in range(start, end, step)]


def binary_search(ordered_list: List[int],
                  required_item: int):
    step: int = 0
    low_value: int = 0
    high_value: int = len(ordered_list)-1
    while low_value <= high_value:
        step += 1
        middle_value = (low_value+high_value)//2
        if required_item == ordered_list[middle_value]:
            return (middle_value, step)
        if required_item > ordered_list[middle_value]:
            low_value = middle_value+1
        else:
            high_value = middle_value-1


def main():
    current_value = 1
    ordered_list: List[int] = create_ordered_list(end=3)
    try:
        result_position, step = binary_search(ordered_list, current_value)
        print(
            f'Result position of {current_value} is {result_position} in list')
        print(f'Searched in {step} steps')
    except TypeError:
        print(f'The list does not contain current value "{current_value}"')


if __name__ == '__main__':
    main()
