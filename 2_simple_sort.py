from random import randint


def find_min(array: list) -> int:
    min_element = 0
    for element_position, element in enumerate(array):
        if element < array[min_element]:
            min_element = element_position
    return min_element


def sort_array(array):

    sorted_array = []
    unsorted_array = array.copy()

    while unsorted_array:
        min_index = find_min(unsorted_array)
        sorted_array.append(unsorted_array.pop(min_index))

    return sorted_array


def main():
    max_value = 100
    test_array = [randint(0, max_value) for random_value in range(max_value)]
    sorted_array = sort_array(test_array)

    print('Unsorted array :', test_array)

    print('Sorted array :', sorted_array)


if __name__ == '__main__':
    main()
