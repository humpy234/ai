#Q1
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

bfs('A')

#Q2
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

# Supervised Learning
X = [[1], [2], [8], [9]]
y = [0, 0, 1, 1]
model = DecisionTreeClassifier()
model.fit(X, y)
print("Supervised:", model.predict([[3]]))

# Unsupervised Learning
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(X)
print("Unsupervised:", kmeans.labels_)
