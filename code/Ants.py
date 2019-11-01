from Ant import *
from readin import *
import numpy as np
from LCS import *
import random
import time
import multiprocessing as mp
from multiprocessing import Process, Lock, Pool

AntNumGPU = 2000
AntNumCPU = mp.cpu_count()
q0 = 0.9
q1 = 0.95
alpha = 1
beta = 2
dirpath = '../dataset/test_data/dna_rat_10/'
SR = readin(dirpath)
n = len(SR)
a, b = random.sample(range(n), 2)
sample1 = SR[a]
sample2 = SR[b]
# c* <- |LCS2(Sx,Sy)|
M = lcs2(sample1, sample2)
print(M)

###################starting parallel computatio###################
# Copy strings to execution device memory
# TO-DO

# Initialize pheromone trails & ant memory
# phero shape [string_num， lengthOf1 string]
# phero在外面更新，只传入进去值
phero = []
# eta shape [string_num， lengthOf1 string]
for i in range(n):
	li = [1.0 for j in range(len(SR[i]))]
	phero.append(li)
# eta shape [string_num， lengthOf1 string]
# eta = phero

start = time.time()
totalBest = ""
# while termination condition not met do
EPOCHS = 100
for epoch in range(EPOCHS):
	currentBest = ""
	# for i in range(10):
	# 	solut = ant_des(phero, SR, q0, q1, alpha, beta, i)
	# 	print(solut)
	# 	print(len(solut))
	# 	if len(currentBest)<len(solut):
	# 		currentBest = solut
	# continue
	solut = ant_des(phero, SR, q0, q1, alpha, beta, 2)
	print(len(solut))
	end = time.time()
	print("%f seconds used!" % (end-start))
	exit()


	pool = Pool()
	# results = []

	lis = np.random.randint(10,size=AntNumCPU)
	for i in range(AntNumCPU):
		# results.append(pool.apply_async(ant_des, (phero, SR, q0, q1, alpha, beta)))
		results = [pool.apply_async(ant_des, (phero, SR, q0, q1, alpha, beta, i)) for i in lis]
	pool.close()
	pool.join()

	# manager = multiprocessing.Manager()
	# return_dict = manager.dict()
	#
	# for _ in range(AntNumCPU):
	# 	p = mp.Process(target=ant_des, args=(phero, eta, SR, q0, q1, alpha, beta))
	# 	p.start()
	# 	results.append(p)
	# for p in results:
	# 	p.join()
	#
	# print(return_dict.values())
	# exit()


	total = 0.0
	for result in results:
		print(result.get())
		if len(result.get()) > total:
			total = len(result.get())
	print('Done')
	print(total)
	exit()

	# lock = Lock()
	# for i in range(AntNumCPU):
	# 	Process(target=ant_des, args=(lock, phero, eta, SR, q0, q1, alpha, beta)).start()


	for i in range(num):
		solu = ant_des(phero, eta, SR, q0, q1, alpha, beta)
		if len(currentBest) < len(solu):
			currentBest = solu

	# update pheromone trail
	# TO-DO
	if len(currentBest)>len(totalBest):
		totalBest = currentBest


end = time.time()
print(len(totalBest))
print("100 epochs used %f s" % (end-start))
