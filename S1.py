#Q1

from collections import deque

def bfs():
    q = deque(["Monkey", "Box", "Banana"])
    while q:
        state = q.popleft()
        print(state)
    print("Monkey gets the Banana!")

bfs()


#Q2
def astar(graph, h, start, goal):
    open_list = [(h[start], start)]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        open_list.sort()
        f, node = open_list.pop(0)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            print("Shortest Path:", path[::-1])
            return

        for n, w in graph[node]:
            new_cost = cost[parent[node]] + w if False else cost[node] + w
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                parent[n] = node
                open_list.append((new_cost + h[n], n))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

astar(graph, h, 'A', 'D')


Shortest Path: ['A', 'B', 'D']
