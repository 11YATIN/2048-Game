import random

def start_game():
    matrix = [[0 for i in range(4)] for j in range(4)]
    return matrix
    
def append_2(matrix):
    x = random.randint(0,3)
    y = random.randint(0,3)
    while matrix[x][y]!=0:
        x = random.randint(0,3)
        y = random.randint(0,3)
    matrix[x][y] = 2
    
def current_state_of_game(matrix):
    # GAME WON
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==2048:
                return "WON"
    # GAME NOT OVER
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return "GAME NOT OVER"
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i][j+1] or matrix[i][j] == matrix[i+1][j]:
                return "GAME NOT OVER"
    for i in range(3):
        if matrix[3][i] == matrix[3][i+1]:
            return "GAME NOT OVER"
    for i in range(3):
        if matrix[i][3] == matrix[i+1][3]:
            return "GAME NOT OVER"
    # GAME LOST
    return "LOST"

def compress(matrix):
    x_matrix = [[0 for i in range(4)] for j in range(4)]
    change = False
    for i in range(4):
        x = 0
        for j in range(4):
            if matrix[i][j]!=0:
                x_matrix[i][x] = matrix[i][j]
                if change is False and x!=j:
                    change = True
                x+=1
    return x_matrix, change

def merge(matrix):
    change = False
    for i in range(4):
        for j in range(3):
            if matrix[i][j]!=0 and matrix[i][j] == matrix[i][j+1]:
                matrix[i][j] *= 2
                matrix[i][j+1] = 0
                change = True
    return matrix, change

def reverse(matrix):
    x_matrix = []
    for i in range(4):
        x_matrix.append([])
        for j in range(4):
            x_matrix[i].append(matrix[i][4-j-1])
    return x_matrix

def transpose(matrix):
    x_matrix = []
    for i in range(4):
        x_matrix.append([])
        for j in range(4):
            x_matrix[i].append(matrix[j][i])
    return x_matrix

def move_left(matrix):
    x,c1 = compress(matrix)
    x,c2 = merge(x)
    c = c1 or c2
    x,t = compress(x) # No need of change in second compression therefore just store it in any random variable
    return x, c

def move_right(matrix):
    x = reverse(matrix)
    x,c1 = compress(x)
    x,c2 = merge(x)
    c = c1 or c2
    x,t = compress(x)
    x = reverse(x)
    return x, c

def move_up(matrix):
    x = transpose(matrix)
    x,c1 = compress(x)
    x,c2 = merge(x)
    c = c1,c2
    x,t = compress(x)
    x = transpose(x)
    return x, c 

def move_down(matrix): 
    x = transpose(matrix)
    x = reverse(x)
    x,c1 = compress(x)
    x,c2 = merge(x)
    c = c1 or c2
    x,t = compress(x)
    x = reverse(x)
    x = transpose(x)
    return x, c
