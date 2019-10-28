def ant_des(phero, eta, SR)
	solution = ""
	# SR: all the n strings
	# total num of strings: n
	# Sr: randomly choosed string
	n = len(SR)
	lengthOfStrings = []
	for i in range(n):
		lengthOfStrings.append(len(SR[i]))
	r = np.random.randint(n)
	Sr = SR[r]
	# U: Current position at n strings
	U = np.zeros(n)
	v = np.zeros(n)
	pf = np.zeros(len(Sr))
	# U[r] is a index, position
	# when U[r] equals len(Sr)-1, it's at the last position of the string, there is no candidate.
	while U[r] <= len(Sr)-2
		# every candidate
	   for k in range(U[r]+1, len(Sr))
	       # char <- character at position c in Sr
	       char = Sr[k]
	        # vc <- calculate next occurrences of character char in all strings
	        for j in range(n)
	            if j != r
	               v[j] = findc(SR[j], char, U[j])
	        # pfc <- calculate probabilistic transition factor pf()
	        pf[k] = pf_c(phero[r], eta[r], k)
	        # update eta
	    eta[r][U[r]+1] =  calEta(v, u, lengthOfStrings)
	    # q <- random number [0, 1)
	    q = np.random.rand()
	    # choose c from Cand by probabilistic function p(v, pf, q)
	    next_p = prob(v, pf, q)
	    # char <- character at position c in Sr
	    nextc = Sr[next_p]
	    if nextc==-1:

	    # solution <- solution U char
	    solution += nextc
	    # update solution position in every strings
	    for i in range(n):
	    	U[i] = v[i]
	return solution


def findc(S, char, uc):
    vc = find(S, uc+1, len(S))
    return vc


def pf_c(phero_sin, eta_sin, candIndex):
    denominator = sum(np.power(phero_sin, alpha)*np.power(eta_sin, beta))
    pfc = phero_sin[candIndex]**alpha*eta_sin[candIndex]**beta/denominator
    return pfc


def calEta(v, u, lenOfStrs):
	eta = 0.0
	for i in range(n):
		eta += (v[i]-u[i]) / (lenOfStrs[i]-u[i])
	return 1.0 / eta


def prob(v, pf, q):
	if q>q1:
		nextp = -1
	elif q<q0:

	else:

	return 


