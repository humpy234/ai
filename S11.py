#Q1
tree = [[3, 5], [6, 9]]

def minimax(tree):
    return max(min(x) for x in tree)

def alpha_beta(tree):
    return max(min(x) for x in tree)

print("Minimax:", minimax(tree))
print("Alpha-Beta:", alpha_beta(tree))


#Q2
rules = {
    "B": ["A"],
    "C": ["B"]
}
facts = ["A"]

def backward(goal):
    if goal in facts:
        return True
    if goal in rules:
        return all(backward(x) for x in rules[goal])
    return False

print("C is", backward("C"))
