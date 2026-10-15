#Q1
from heapq import heappush, heappop

goal = (1, 2, 3, 0)

def heuristic(s):
    return sum(abs(i//2 - (x-1)//2) + abs(i%2 - (x-1)%2)
               for i, x in enumerate(s) if x)

def astar(start):
    q = [(heuristic(start), 0, start)]
    visited = set()

    while q:
        f, g, s = heappop(q)
        if s == goal:
            print("Goal Reached:", s)
            return

        if s in visited:
            continue
        visited.add(s)
        i = s.index(0)

        for j in [i-2, i+2, i-1, i+1]:
            if 0 <= j < 4 and abs(i//2-j//2)+abs(i%2-j%2) == 1:
                t = list(s)
                t[i], t[j] = t[j], t[i]
                t = tuple(t)
                if t not in visited:
                    heappush(q, (g+1+heuristic(t), g+1, t))

start = (1, 2, 0, 3)
astar(start)

#Q2 OR

temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("It is hot. Drink more water.")
elif temperature > 20:
    print("Weather is pleasant.")
else:
    print("It is cold. Wear warm clothes.")
