#Q1
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for child in graph[node]:
            dfs(graph, child, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

dfs(graph, 'A', set())


#Q2 
from sklearn.svm import SVC
X = [[1, 2], [2, 3], [5, 5]]
y = [0, 0, 1]
model = SVC(kernel='rbf')
model.fit(X, y)
test = [[4, 4]]
print("Predicted Class:", model.predict(test)[0])

