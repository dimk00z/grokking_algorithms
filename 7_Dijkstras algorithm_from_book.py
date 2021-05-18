from utils import measure
from pprint import pprint

INFINITY = float('inf')


def find_lowest_cost_node(costs, processed):
    lowest_cost = INFINITY
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


@measure
def main():

    graph = {
        'start': {
            'a': 6,
            'b': 2,
        },
        'a': {
            'fin': 1,
        },
        'b': {
            'a': 3,
            'fin': 5,
        },
        'fin': {}
    }
    costs = {
        'a': 6,
        'b': 2,
        'fin': INFINITY,
    }
    parents = {
        'a': 'start',
        'b': 'start',
        'fin': None
    }
    processed = []
    node = find_lowest_cost_node(costs, processed)
    print(node)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(node)
    pprint(costs)
    pprint(parents)


if __name__ == "__main__":
    main()
