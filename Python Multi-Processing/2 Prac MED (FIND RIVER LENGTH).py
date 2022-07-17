# We will be using depth first search
def riverSizes(matrix):
    marked = set()
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1 and (row,col) not in marked:
                cur_river_len = 1
                marked.add((row,col))
                stack = [(row,col)]

                while stack:
                    curr = stack.pop()
                    neighbors = get_neighbors(curr,matrix)
                    for n in neighbors:
                        y,x = n
                        if matrix[y][x]==1 and (y,x) not in marked:
                            marked.add((y,x))
                            cur_river_len+=1
                            stack.append((y,x))

                rivers.append(cur_river_len)

    return rivers



def get_neighbors(pos, matrix):
    y, x = pos
    ns = []
    if x >= 1:
        ns.append((y,x-1))
    if x<len(matrix[0])-1:
        ns.append((y,x+1))

    if y >= 1:
        ns.append((y-1,x))
    if y<len(matrix)-1:
        ns.append((y+1,x))

    return ns

