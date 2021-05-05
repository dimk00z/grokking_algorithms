from utils import create_ordered_list


def binary_search_with_recursion(
        ordered_list, required_item, left, right):
    if right >= left:
        middle = (left+right)//2
        # print(middle, ordered_list[middle])
        if ordered_list[middle] == required_item:
            return middle
        elif ordered_list[middle] > required_item:
            return binary_search_with_recursion(
                ordered_list, required_item, left, middle-1)
        else:
            return binary_search_with_recursion(
                ordered_list, required_item, middle+1, right)


def main():
    ordered_list = create_ordered_list(end=10)
    position = binary_search_with_recursion(
        ordered_list, required_item=10,
        left=0, right=(len(ordered_list)-1))
    # print(position)
    if position is not None:
        print('Position is', position+1)
        print(*ordered_list)
    else:
        print('Required item is not in the list')


if __name__ == '__main__':
    main()
