from utils import create_ordered_list


def binary_search(ordered_list, required_item):

    def binary_search_with_recursion(
            ordered_list, required_item, left, right):
        middle = (left+right)//2

        # basic case
        if ordered_list[middle] == required_item:
            return middle

        # recursive case
        if ordered_list[middle] > required_item:
            return binary_search_with_recursion(
                ordered_list, required_item, left, middle-1)
        else:
            return binary_search_with_recursion(
                ordered_list, required_item, middle+1, right)

    position = binary_search_with_recursion(
        ordered_list, required_item, left=ordered_list[0], right=ordered_list[-1])
    if position is not None:
        print('Position is', position+1)
        print(*ordered_list)
    else:
        print('Required item is not in the list')


def main():
    ordered_list = create_ordered_list(end=10)
    binary_search(ordered_list=ordered_list, required_item=10)


if __name__ == '__main__':
    main()
