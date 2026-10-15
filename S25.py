#Q1
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [], 'F': [], 'G': []
}

cost = {'A': 1, 'B': 1, 'C': 1, 'D': 1,
        'E': 0, 'F': 0, 'G': 0}

def ao_star(node):
    if not graph[node]:
        return cost[node]
    cost[node] = min(
        sum(ao_star(n) for n in group)
        for group in graph[node]
    )
    return cost[node]

print("Minimum cost:", ao_star('A'))

#Q2 OR
facts = ['A']
rules = {'A': 'B', 'B': 'C'}

def forward():
    while True:
        new = False
        for x, y in rules.items():
            if x in facts and y not in facts:
                facts.append(y)
                new = True
        if not new:
            break

forward()
print("Facts:", facts)

