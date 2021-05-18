from utils import measure
from pprint import pprint
from copy import copy

INFINITY = float('inf')


def search_lowest_cost_node():
    pass


def deijtra_rearch(graph, start, finish):
    if start == finish:
        print('Start and finish must be different nodes')
        return None
    pprint(graph)
# https://question-it.com/questions/1482965/algoritm-dejkstry-python

    costs = {}
    for node in graph.keys():
        costs[node] = 0 if node == start else INFINITY
    print(costs)
    processed = []
    processed.append(node)
    # for node for graph[node]:

    return None


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
    deijtra_rearch(graph, 'a', 'f')


if __name__ == "__main__":
    main()
