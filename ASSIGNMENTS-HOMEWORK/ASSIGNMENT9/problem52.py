def footpath_cost(matrix, queries):
    n = len(matrix)
    m = len(matrix[0])
    
    results = []
    
    for r, c in queries:
        r -= 1  # convert to 0-based
        c -= 1
        
        sections = []
        
        # top-left
        if r > 0 and c > 0:
            sections.append(min(matrix[i][j] for i in range(0, r) for j in range(0, c)))
        
        # top-right
        if r > 0 and c < m-1:
            sections.append(min(matrix[i][j] for i in range(0, r) for j in range(c+1, m)))
        
        # bottom-left
        if r < n-1 and c > 0:
            sections.append(min(matrix[i][j] for i in range(r+1, n) for j in range(0, c)))
        
        # bottom-right
        if r < n-1 and c < m-1:
            sections.append(min(matrix[i][j] for i in range(r+1, n) for j in range(c+1, m)))
        
        results.append(sum(sections) if sections else min(min(row) for row in matrix))
    
    return results
