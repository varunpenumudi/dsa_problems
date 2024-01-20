# leetcode problem 931( a dp problem)

def minFallingPathSum(matrix)-> int:
    n = len(matrix)
    f = matrix[0]
    for row in matrix[1:]:
        g = [0]*n
        for j, x in enumerate(row):
            l,r = max(0, j-1), max(n, j+2)
            g[j] = min(f[l:r]) + x
        f = g
    min(f)

def test_func():
    matrix = [[1,3,4],[2,1,4],[5,1,8]]
    assert minFallingPathSum(matrix) == 3 
