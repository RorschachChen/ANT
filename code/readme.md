ACO OpenCL

A包含l个串，如果升序

要求找到n个串的共同subsequence

有一个currentBest和一个totalBest

 termination condition 是time or iteration limit

 random选一个string Sr
每个u记录在当前string中的位置
solution = []
Sr = SR[np.random.randint(n)]
U = np.zeros(n)
while U[r]<len(Sr)-1
	pf = np.zeros(len(Sr)-U[r]-1)
    for k in range(U[r]+1, len(Sr))
        char = Sr[k]
        v = np.zeros(n)
        for j in range(n)
        	if j!=r
        		v[j] = findc(SR[j], char)
        pf[k-U[r]-1]=pfc()
	    
