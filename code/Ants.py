from Ant import *
from readin import *
import numpy as np

AntNum = 2000
n = 10
q0 = 0.9
q1 = 0.95
alpha = 1
beta = 2
dirpath = '../dataset/test_data/dna_rat_10/'
SR = readin()
# phero shape [string_num， lengthOf1 string]
phero = []# eta shape [string_num， lengthOf1 string]
for i in range(n):
	li = [1.0 for j in range(len(SR[i]))]
	phero.append(li)
# eta shape [string_num， lengthOf1 string]
eta = phero

currentBest = ant_des(phero, eta, SR, q0, q1, alpha, beta)

for i in range(AntNum):
	solu = ant_des(phero, eta, SR, q0, q1, alpha, beta)
	if len(currentBest)<len(solu):
		currentBest = solu

print(len(currentBest))
