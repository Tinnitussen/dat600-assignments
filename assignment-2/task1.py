def matrix_chain_order(p):
    n = len(p) - 1
    
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # Start with chain length 2 up to the full chain length
    for l in range(2, n+1):
        # Consider all possible chains of length l
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = float("inf")
            # Try different splits and record the minimum cost
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m, s

def print_optimal_parenthesis(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        return f"({print_optimal_parenthesis(s, i, s[i][j])} × {print_optimal_parenthesis(s, s[i][j]+1, j)})"

if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20]
    m, s = matrix_chain_order(p)
    
    print(f"Minimum number of scalar multiplications: {m[1][len(p)-1]}")
    print(f"Optimal parenthesization: {print_optimal_parenthesis(s, 1, len(p)-1)}")