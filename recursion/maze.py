from stack import Stack

size: int = 5
matrix =  [[0 for x in range(size)] for y in range(size)] 

'''
0 - not visited
1 - visited
2 - obstacle
'''
# place maze obstacles
matrix[0][2] = 2
matrix[0][3] = 2
matrix[1][0] = 2
matrix[2][2] = 2
matrix[2][3] = 2
matrix[2][4] = 2
matrix[3][1] = 2
matrix[4][3] = 2

# starting position
matrix[0][0] = 1 

stack = Stack()
stack.push([0, 0])

def mazeSolver(matrix: list, stack: Stack):
    if stack.isEmpty():
        print("Path not found")
    else:
        coords: list = stack.peek()
        x = coords[0]
        y = coords[1]
        if x == len(matrix) - 1 and y == len(matrix[x]) - 1:
            print("Path found")
        elif y < len(matrix[x]) - 1 and matrix[x][y + 1] == 0: # can go right
            matrix[x][y + 1] = 1 # mark as visited
            stack.push([x, y + 1])
            mazeSolver(matrix, stack)
        elif y > 0 and matrix[x][y - 1] == 0: # can go left
            matrix[x][y - 1] = 1 # mark as visited
            stack.push([x, y - 1])
            mazeSolver(matrix, stack)
        elif x < len(matrix) - 1 and matrix[x + 1][y] == 0: # can go down
            matrix[x + 1][y] = 1 # mark as visited
            stack.push([x + 1, y])
            mazeSolver(matrix, stack)
        elif x > 0 and matrix[x - 1][y] == 0: # can go up
            matrix[x - 1][y] = 1 # mark as visited
            stack.push([x - 1, y])
            mazeSolver(matrix, stack)
        else:
            stack.pop()
            mazeSolver(matrix, stack)

mazeSolver(matrix, stack)