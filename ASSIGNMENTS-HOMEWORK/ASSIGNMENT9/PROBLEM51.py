def prefix_sum_2d(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # Create prefix sum matrix
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (
                matrix[i-1][j-1]
                + prefix[i-1][j]
                + prefix[i][j-1]
                - prefix[i-1][j-1]
            )
    
    return prefix


def query_sum(prefix, r1, c1, r2, c2):
    # Convert to 1-based indexing
    r1 += 1
    c1 += 1
    r2 += 1
    c2 += 1
    
    return (
        prefix[r2][c2]
        - prefix[r1-1][c2]
        - prefix[r2][c1-1]
        + prefix[r1-1][c1-1]
    )


# Example usage
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries = [
    [0, 0, 1, 1],  # sum of submatrix from (0,0) to (1,1)
    [1, 1, 2, 2]   # sum of submatrix from (1,1) to (2,2)
]

prefix = prefix_sum_2d(a)

for q in queries:
    print(query_sum(prefix, q[0], q[1], q[2], q[3]))
