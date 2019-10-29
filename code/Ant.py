import numpy as np

def ant_des(phero, eta, SR, q0, q1, alpha, beta):
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
    U = np.zeros(n, dtype=np.uint8)
    pf = np.zeros(len(Sr))
    # for exploitation in probabilistic function, there is no need to divide by sum of pf
    pf2 = np.zeros(len(Sr))
    # U[r] is a index, position
    # when U[r] equals len(Sr)-1, it's at the last position of the string, there is no candidate.
    # U will be updated every epochs in while loop. 
    # pf will be updated every epochs in while loop. 
    while U[r] <= len(Sr)-2:
        # v should have 2 dims, after prob function, we need the final position in each string of best candidate.
        # (len(Sr), n)
        v = np.zeros((len(Sr), n))
        # every candidate
        for k in range(U[r]+1, len(Sr)):
            # char <- character at position c in Sr
            ch = Sr[k]
            # vc <- calculate next occurrences of character char in all strings
            for j in range(n):
                if j != r:
                    v[k][j] = findc(SR[j], ch, U[j])
                else:
                    v[k][j] = k
            # when v changes, eta2 must be updated instantly. "eta2[r][c]"
            eta[r][k] =  calEta(v[k], U, lengthOfStrings)
            # pfc <- calculate probabilistic transition factor pf()
            pf[k], pf2[k] = pf_c(phero[r], eta[r], k, alpha, beta)
            # update eta
        # q <- random number [0, 1)
        q = np.random.rand()
        # choose c from Cand by probabilistic function p(v, pf, q)
        next_p = prob(pf, pf2, q, q0, q1)
        if next_p==-1:
            break
        # print(next_p)
        # char <- character at position c in Sr
        nextc = Sr[next_p]
        # solution <- solution U char
        solution += nextc
        # update solution position in every strings
        for i in range(n):
            U[i] = v[next_p][i]
    return solution


def findc(S, ch, uc):
    vc = S.find(ch, uc+1, len(S))
    return vc


def pf_c(phero_sin, eta_sin, candIndex, alpha, beta):
    denominator = sum(np.power(phero_sin, alpha)*np.power(eta_sin, beta))
    pfc = phero_sin[candIndex]**alpha*eta_sin[candIndex]**beta/denominator
    pfc2 = phero_sin[candIndex]**alpha*eta_sin[candIndex]**beta
    return pfc, pfc2


def calEta(v, u, lenOfStrs):
    # Be careful
    eta = 0.0
    n = len(lenOfStrs)
    for i in range(n):
        eta += (v[i]-u[i]) / (lenOfStrs[i]-u[i]-1)
    return 1.0 / eta


def prob(pf, pf2, q, q0, q1):
    if q>q1:
        nextp = -1
    elif q<q0:
        nextp = np.argmax(pf2)
    else:
        nextp = np.argmax(pf )
    return nextp


