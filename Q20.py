#Q1
def f(x):
    return -x**2 + 6*x

def hill_climbing(x):
    while True:
        if f(x + 1) > f(x):
            x += 1
        elif f(x - 1) > f(x):
            x -= 1
        else:
            return x, f(x)

x, maximum = hill_climbing(0)
print("Maximum value:", maximum)
print("At x =", x)

#Q2 OR
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

X = [[1], [2], [8], [9]]
y = [0, 0, 1, 1]

# Supervised Learning
model = DecisionTreeClassifier()
model.fit(X, y)
print("Supervised:", model.predict([[3]]))

# Unsupervised Learning
km = KMeans(n_clusters=2, random_state=0, n_init=10)
km.fit(X)
print("Unsupervised:", km.labels_)
