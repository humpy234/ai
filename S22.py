#Q!
def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(source, "->", target)
        return
    hanoi(n-1, source, target, auxiliary)
    print(source, "->", target)
    hanoi(n-1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')

#Q2 OR
def solve(board, row, n):
    if row == n:
        print(board)
        return True

    for col in range(n):
        if all(board[i] != col and
               abs(board[i] - col) != row - i
               for i in range(row)):
            board[row] = col
            if solve(board, row + 1, n):
                return True
    return False

n = 4
solve([-1] * n, 0, n)
