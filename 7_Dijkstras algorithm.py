from pprint import pprint
from copy import copy

INFINITY = float('inf')


def deijtra_rearch(graph, start, finish):
    if start == finish:
        return 'Start and finish must be different nodes'
    pprint(graph)

    costs = {}
    updated_nodes = {}
    for node in graph.keys():
        costs[node] = 0 if node == start else INFINITY
    temp_costs = copy(costs)
    while len(temp_costs) > 0:
        min_node = min(temp_costs, key=temp_costs.get)
        for neighbor in graph[min_node]:
            cost_to_neighbor = costs[min_node] + graph[min_node][neighbor]
            if costs[neighbor] > cost_to_neighbor:
                costs[neighbor] = cost_to_neighbor
                temp_costs[neighbor] = cost_to_neighbor
                updated_nodes[neighbor] = min_node

        del temp_costs[min_node]

    path = []
    node = finish
    while True:
        path.append(node)
        if node in updated_nodes:
            node = updated_nodes[node]
        else:
            print(f'There is no path from {start} to {finish}.')
        if node == start:
            path.append(node)
            break
    shortest_path = ' > '.join(path[::-1])
    result_string = f'''The shortest path from {start} to {finish}: {shortest_path} and the weight is {costs[finish]}'''
    return result_string


def main():
    graph = {
        'a': {
            'b': 10,
            'c': 6,
        },
        'b': {
            'a': 10,
            'c': 3,
            'd': 4,
            'e': 1,
            'f': 8,
        },
        'c': {
            'a': 6,
            'b': 3,
            'd': 7,
        },
        'd': {
            'c': 7,
            'b': 4,
            'e': 11,
            'f': 7,
        },
        'e': {
            'b': 1,
            'd': 11,
            'f': 3,
        },
        'f': {
            'b': 8,
            'e': 3,
            'd': 7,
        }
    }
    print(deijtra_rearch(graph, 'a', 'f'))


if __name__ == "__main__":
    main()
