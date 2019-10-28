AntNum = 2000
n = 10

from Ant import *
import numpy as np
SR = ""
# phero shape [string_num， lengthOf1 string]
phero = []
for i in range(n):
	li = [1.0 for j in range(len(SR[i]))]
	phero.append(li)
# eta shape [string_num， lengthOf1 string]
eta = []
for i in range(n):
	eta.append(li)

currentBest = ant_des(phero, eta)

for i in range(AntNum):
	solu = ant_des(phero, eta)
	if len(currentBest)<len(solu):
		currentBest = solu
