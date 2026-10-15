#Q1
import heapq

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'],
         'D': [], 'E': []}
h = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

def best_first(start, goal):
    pq = [(h[start], start)]
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)

        if node == goal:
            return
        for n in graph[node]:
            if n not in visited:
                heapq.heappush(pq, (h[n], n))

best_first('A', 'E')


#Q2
p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("IMPLIES:", (not p) or q)
