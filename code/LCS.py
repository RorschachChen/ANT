#!/usr/bin/env python

import time
def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 

X = "AGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAGGTAB"
Y = "GXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYB"

def lcs2(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs2


# Dynamic programming implementation of LCS problem 
  
# Returns length of LCS for X[0..m-1], Y[0..n-1]  
def lcs_str(X, Y, m, n): 
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)] 
  
    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in xrange(m+1): 
        for j in xrange(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following code is used to print LCS 
    index = L[m][n] 
  
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
  
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))
  
# Driver program 
# X = "AGGTAB"
# Y = "GXTXAYB"

start = time.time()
print("Length of LCS is ", lcs2(X, Y))
print(time.time()-start)

# m = len(X)
# n = len(Y)
# k = lcs(X, Y, m, n)
# print(k)
# This code is contributed by BHAVYA JAIN 


