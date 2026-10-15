#Q1
def f(x):
    return -x**2 + 6*x

x = 0

while f(x + 1) > f(x):
    x += 1

print("Maximum value:", f(x))
print("At x =", x)

#Q2
facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D")
]

while True:
    new_fact = False
    for condition, result in rules:
        if condition.issubset(facts) and result not in facts:
            facts.add(result)
            new_fact = True
    if not new_fact:
        break

print("Facts:", facts)
