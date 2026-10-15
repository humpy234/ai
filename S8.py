#Q1
def astar(graph, h, start, goal):
    open_list = [(h[start], start)]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        open_list.sort()
        _, node = open_list.pop(0)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            print("Shortest Path:", path[::-1])
            return

        for n, w in graph[node]:
            new_cost = cost[node] + w
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                parent[n] = node
                open_list.append((new_cost + h[n], n))

graph = {
    'V1': [('V2', 2), ('V3', 4)],
    'V2': [('V4', 3), ('V5', 5)],
    'V3': [('V5', 2)],
    'V4': [('V6', 4)],
    'V5': [('V6', 3)],
    'V6': []
}
h = {'V1': 7, 'V2': 5, 'V3': 4,
     'V4': 3, 'V5': 2, 'V6': 0}

#Q2 OR
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def solve(node):
    if node not in color:
        for c in colors:
            if all(color.get(n) != c for n in graph[node]):
                color[node] = c
                if len(color) == len(graph):
                    return True
                if solve(next(n for n in graph if n not in color)):
                    return True
                del color[node]
        return False
    return True

solve('A')
print(color)


Output:

{'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}
astar(graph, h, 'V1', 'V6')
