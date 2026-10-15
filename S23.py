#Q1
def f(x):
    return -x**2 + 4*x

x = 0
while f(x + 0.1) > f(x):
    x += 0.1

print("Maximum value:", round(f(x), 2))
print("At x =", round(x, 1))

#Q2 OR
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

X = [[1], [2], [8], [9]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)
print("Supervised:", model.predict([[3]]))

km = KMeans(n_clusters=2, random_state=0, n_init=10)
km.fit(X)
print("Unsupervised:", km.labels_)
