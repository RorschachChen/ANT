import numpy as np


def ant_des_v2(phero, SR, q0, q1, alpha, beta, lis):
    d = 10
    solution = ""
    # SR: all the n strings
    # total num of strings: n
    # Sr: randomly choosed string
    n = len(SR) # 10
    # lengthOfStrings = []
    # lengthOfStrings = 600*np.ones(n)
    # for i in range(n):
    #     lengthOfStrings.append(len(SR[i])) # 所有string的长度
    # [1740, 1070, 1054, 1048, 1446, 1021, 1419, 1405, 1401, 1090]
    # r = np.random.randint(n)
    #
    r = lis
    print(r)
    # print(len(SR[r]))
    # eta = []
    # for i in range(n):
    #     li = [1.0 for j in range(lengthOfStrings[i])]
    #     eta.append(li)
    # eta shape [string_num， lengthOf1 string]

    Sr = SR[r]
    # U: Current position at n strings
    U = np.zeros(n, dtype=np.uint16)
    # pf = np.zeros(len(Sr))
    # for exploitation in probabilistic function, there is no need to divide by sum of pf
    # pf2 = np.zeros(len(Sr))
    # U[r] is a index, position
    # when U[r] equals len(Sr)-1, it's at the last position of the string, there is no candidate.
    # U will be updated every epochs in while loop. 
    # pf will be updated every epochs in while loop. 
    while U[r] < len(Sr)-1:
        # print("Now U is at %d" % U[r])
        # v should have 2 dims, after prob function, we need the final position in each string of best candidate.
        resCand = min(U[r]+d, len(Sr)-1)
        res = resCand - U[r]
        v = np.zeros((res, n))
        eta2 = np.zeros(res)
        # pf每次移位后尺寸都会变化
        # 事实证明pf和pf2并无区别，效果完全一样
        pf = np.zeros(res)
        pf2 = np.zeros(res)
        # every candidate
        for k in range(U[r]+1, resCand+1):
            # char <- character at position c in Sr
            ch = Sr[k]
            # vc <- calculate next occurrences of character char in all strings
            # flag = 0
            ind = k-U[r]-1
            # ind从0到d-1
            for j in range(n):
                if j != r:
                    pos_in_each_string = findc(SR[j], ch, U[j])
                    if pos_in_each_string != -1:
                        v[ind][j] = pos_in_each_string
                    # 这个char必须在所有的串中有下一个才行，不然这个cand直接作废
                    else:
                        v[k-U[r]-1][j] = len(SR[j])-1 # 599
                        # break
                    # 第k个dim是n，存的是这个cand的字符在所有字符串中的下一个,如果没有则是-1
                elif j==r:
                    v[k-U[r]-1][j] = k
            # if flag == 1:
            # 如果不是全都有的话，eta被设置为0，接下来pfc一定会等于0，cand作废
            # 把这一个cand的eta设置为0
                # eta2[k-U[r]-1] = 0
            # when v changes, eta2 must be updated instantly. "eta2[r][c]"
            # update eta
            # 输入的dim [n, n]
            # 对于每一个cand，v都不一样，但是U是一样的
            # eta[r][k] = calEta(v[k-U[r]-1], U, lengthOfStrings)
            # else:
            # n, n 
            eta2[ind] = calEta(v[ind], U, n)
            # pfc <- calculate probabilistic transition factor pf()
            # phero只累加当前U的后面所有candidate，而不是整个第r个字符串的
        # 要在所有的eta都设置好了之后再计算pfc

        ############################################################
        # 有一个考察因素就是看这个变量是否可覆盖，之后是否需要再次用到。
        ############################################################

        # 针对所有的cand，计算每个的pfc
        for k in range(U[r]+1, resCand+1):
            ind = k-U[r]-1
            # pf[k], pf2[k] = pf_c(phero[r][U[r]+1:], eta[r][U[r]+1:], k-U[r]-1, alpha, beta)
            # phero[r][U[r] + 1:]第r条，所有cand位置的信息素
            pf[ind], pf2[ind] = pf_c(phero[r][U[r] + 1:U[r]+res+1], eta2, ind, alpha, beta)
        # q <- random number [0, 1)
        q = np.random.rand()
        # choose c from Cand by probabilistic function p(v, pf, q)
        # pf和pf2的length都是resCand

        next_p = prob(pf, pf2, q, q0, q1)
        # next_p = np.argmax(pf2)

        # print("It's at nextp(referenced position) %d" % next_p)

        # next_p是相对位置
        # if next_p == -1:
        #     break
        # print(next_p)
        # char <- character at position c in Sr
        next_abs_p = next_p + U[r]+1 # 绝对位置，由cand的index加上目前定位
        # print("It's at nextp(absolute position) %d" % next_abs_p)

        nextc = Sr[next_abs_p] # 具体char
        # solution <- solution U char
        solution += nextc
        # update solution position in every strings
        for i in range(n):
            # v的第一维是cand的长度，确定选中哪个cand后，取出对应所有n串的位置，更新U
            U[i] = v[next_p][i]

        # if one of the positions U[i[ reaches the end of the string, then we should stop right now. ]
        flag = 0
        for i in range(n):
            if U[i]>len(SR[i])-2:
                flag = 1
                break
        if flag == 1:
            break
    # print(len(eta[r]))
    # print(eta[r])
    # print(phero[6])
    return solution


def findc(S, ch, uc):
    vc = S.find(ch, uc+1, len(S))
    return vc


def pf_c(phero_sin, eta_sin, candIndex, alpha, beta):
    # phero_sin和eta_sin都是cand的长度
    denominator = sum(np.power(phero_sin, alpha)*np.power(eta_sin, beta))
    # if denominator == 0:
    #     print("WoW, denominator could be zero!")
    #     print(eta_sin)
    #     exit()
    #     pfc = 0
    #     pfc2 = 0
    # else:
    pfc = phero_sin[candIndex]**alpha*eta_sin[candIndex]**beta / denominator
    pfc2 = phero_sin[candIndex]**alpha*eta_sin[candIndex]**beta
    return pfc, pfc2


def calEta(v, u, numOfStr):
    # Be careful
    eta = 0.0
    for i in range(numOfStr):
        # if lenOfStrs[i]-u[i]-1==0:
        #     eta += 1.0
        # # U[r]是被限制的不能到最后一位，但是可能随着移动位置，其他串的U被移到了其他行的最后一位上，这样就会出现分母为0的情况，但是这种情况，也说明此时这条string的v已经没了，找不到-1
        # else:
        eta += (float(v[i]-u[i])) / (600-u[i]-1)
    return 1.0 / eta


def prob(pf, pf2, q, q0, q1):
    if q>q1:
        nextp = len(pf)-1
    elif q<q0:
        nextp = np.argmax(pf2)
    else:
        nextp = np.argmax(pf)
    return nextp


