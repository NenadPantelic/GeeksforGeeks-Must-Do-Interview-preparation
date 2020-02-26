#code
def is_safe(board, row, col):
    #if row < 0 or row >= n or col < 0 or col >= n:
    #    return False
    # we check only the left side of the position, because we place queens on board column by column
    # check the row 
    for i in range(col):
        if board[row][i] == 1:
            return False
    # check the main diag
    i = row-1; j = col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # check the second diag
    i = row; j = col
    # left lower corner
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True
    
        
    
    
def nqueen(n):
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve(board, n, solutions, 0, [])
    if len(solutions) == 0:
        print(-1)
        return
    for i in range(len(solutions)):
        solutions[i] = "[" + " ".join([str(val) for val in solutions[i]]) + " ]" 
        print(solutions[i], end=" ")
    
    print()

   
    
def solve(board, n, solutions, col, solution):
    # we completed all of the columns
    if col >= n:
        solutions.append(solution)
        return True
    # iterate over rows
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            # for only one solution
            #if solve(board, n, solutions, col+1, solution+str(i+1)):
            #    return True
            # for all solutions
            solve(board, n, solutions, col+1, solution+[i+1])
            #    return True
            # backtrack
            board[i][col] = 0
    return False

   
        
# # Test 1
# n = 2
# nqueen(n)
        
# # Test 2

# n = 4
# nqueen(n)

# # Test 3
# n = 6
# nqueen(n)

# # Test 4
# n = 3 # no solution
# nqueen(n)

# Testing
t = int(input())
for i in range(t):
    n = int(input())
    nqueen(n)
    #print()