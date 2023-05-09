def lcs(X , Y):     
    m = len(X)
    n = len(Y)
    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]

    # retriveing the LCS
    res = ''
    i = m 
    j = n 
    while i > 0 and j > 0:
        if L[i][j] > L[i-1][j-1]:
            res = res + X[i-1]
            i -=1
            j -=1
        else:
            if L[i][j] == L[i-1][j]:
                i -= 1
            else:
                j -= 1
    
    res = res[::-1]
    # L[m][n] is the length of the LCS
    # res is the LCS
    return L[m][n], res

if __name__ == '__main__':
    LCS = lcs('intention','execution')
    print('LCS: ',LCS)