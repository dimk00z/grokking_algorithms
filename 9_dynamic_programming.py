from utils import print_2d_list, get_matrix


def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(area, value, capacity):
    size = len(value)
    table = [
        [0 for _ in range(capacity+1)]
        for _ in range(size+1)]
    for x in range(size+1):
        for y in range(capacity+1):
            if not x or not y:
                table[x][y] = 0
            elif area[x-1] <= y:
                table[x][y] = max(value[x-1] + table[x-1][y-area[x-1]],
                                  table[x-1][y])
            else:
                table[x][y] = table[x-1][y]
    return table


def get_selected_items_list(area, value, capacity, table, stuffdict):
    n = len(value)
    res = table[n][capacity]
    available_capacity = capacity
    items_list = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i-1][available_capacity]:
            continue
        else:
            items_list.append((area[i-1], value[i-1]))
            res -= value[i-1]
            available_capacity -= area[i-1]
    selected_stuff = []
    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)
    return selected_stuff


def robot_paths(n: int, m: int) -> int:
    path_table = get_matrix(n, m)

    def path(n, m, path_table):
        if path_table[n][m] != 0:
            return path_table[n][m]
        if n < 1 or m < 1:
            return 0
        if n == 1 and m == 1:
            return 1
        path_table[n][m] = path(n-1, m, path_table) + path(n, m-1, path_table)
        return path_table[n][m]
    paths_number = path(n, m, path_table)
    print_2d_list(path_table)
    return paths_number


def main():
    stuffdict = {'couch_s': (300, 75),
                 'couch_b': (500, 80),
                 'bed': (400, 100),
                 'closet': (200, 50),
                 'bed_s': (200, 40),
                 'desk': (200, 70),
                 'table': (300, 80),
                 'tv_table': (200, 30),
                 'armchair': (100, 30),
                 'bookshelf': (200, 60),
                 'cabinet': (150, 20),
                 'game_table': (150, 30),
                 'hammock': (250, 45),
                 'diner_table_with_chairs': (250, 70),
                 'stools': (150, 30),
                 'mirror': (100, 20),
                 'instrument': (300, 70),
                 'plant_1': (25, 10),
                 'plant_2': (30, 20),
                 'plant_3': (45, 25),
                 'sideboard': (175, 30),
                 'chest_of_drawers': (25, 40),
                 'guest_bed': (250, 40),
                 'standing_lamp': (20, 30),
                 'garbage_can': (30, 35),
                 'bar_with_stools': (200, 40),
                 'bike_stand': (100, 80),
                 'chest': (150, 25),
                 'heater': (100, 25)
                 }
    area, value = get_area_and_value(stuffdict=stuffdict)
    capacity = 2000
    table = get_memtable(area, value, capacity)
    stuff = get_selected_items_list(area, value, capacity, table, stuffdict)
    print(stuff)
# https://proglib.io/p/python-i-dinamicheskoe-programmirovanie-na-primere-zadachi-o-ryukzake-2020-02-04
    print(robot_paths(3, 7))


if __name__ == '__main__':
    main()
