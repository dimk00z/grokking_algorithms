from collections import deque


def search():
    search_queue = deque()


def person_is_seller(name):
    return name[-1] == 'm'


def breadth_first_search(graph, func):
    searched = []
    search_queue = deque()
    search_queue += graph['you']
    step = 1
    print(search_queue)
    while search_queue:
        person = search_queue.popleft()
        print()
        print('Step #', step)
        print('Person ', person)
        print('Queue ', search_queue)
        print('Searched ', searched)
        if func(person):
            print(person, "is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
        step += 1
    return False


def main():
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['jonny'] = []
    graph['thom'] = []
    graph['peggy'] = []
    graph['anuj'] = []
    print(breadth_first_search(graph, person_is_seller))


if __name__ == "__main__":
    main()
