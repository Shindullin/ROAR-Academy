def swap_rows(M, a, b):
    for i in len(M[a]):
        storage = M[a][i]
        M[a][i]=M[b][i]
        M[b][i]=storage
def swap_col(M,a,b):
    for i in len(M):
        storage = M[i][a]
        M[i][a]=M[i][b]
        M[i][b]=storage