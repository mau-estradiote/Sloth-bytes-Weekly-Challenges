def spiral_Order(matrix):
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    spiral = []
    if n>m:
        k = 2*m-1
    else:
        k = 2*n
    N = k//4+1
    for i in range(N):
        spiral.extend(matrix[0][:])
        spiral.extend([row[-1] for row in matrix[1:]])
        spiral.extend(list(reversed(matrix[-1][1:-1])))
        spiral.extend([row[0] for row in  reversed(matrix[1:])])
        matrix = matrix[1:-1]
        matrix = [row[1:-1] for row in matrix]
        print(matrix)
        if (not matrix) or (not matrix[0]):
            break
    spiral = [l for l in spiral if l]
    return spiral[0:(n*m)]