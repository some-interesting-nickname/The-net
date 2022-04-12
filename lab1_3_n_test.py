import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

def reply(p_r):
	x = np.random.uniform(0,1)

	if(x > p_r):
		return 1
	else:
		return 0

def send(p):
	x = np.random.uniform(0,1)

	if(x > p):
		return 1
	else:
		return 0

def check(p, p_r):
	x = np.random.uniform(0,1)

	if(send(p) and reply(p_r)):
		return 0
	else:
		return 1

def find_average(p, p_r, n):
	count = 1
	while(check(p, p_r) and (count < n)):
		count = count + 1
	return count

def find_average_big(p, p_r, n):
	count_all = 0
	for i in range(0,1000):
		count_all = count_all + find_average(p, p_r, n)

	result = count_all/1000
	return result

def main():
	#print("Enter p: ")
	#p = float(input())

	#count_all = 0
	#for i in range(0,1000):
	#	count_all = count_all + find_average(p)

	#result = count_all/1000
	#print("Average number of requests:" + str(result))

	#print("Enter n: ")
	#n = float(input())

	#print("Enter p_ret: ")
	#p_r = float(input())

	print("Enter n: ")
	n = float((input()))

	x = []
	y = []

	p_r = 0.3
	for p in np.arange(0, 1, 0.099):
		y.append((1-(1-(1-p)*(1-p_r))**n)/((1-p)*(1-p_r)))
		x.append(p)

	for p in np.arange(0, 1, 0.099):
		N = find_average_big(p, p_r, n)
		plt.scatter(p, N)

	plt.plot(x, y, label = "p_ret = 0.3")
	plt.xlabel('p')
	plt.ylabel('N')
	plt.title('N(p)')

	x = []
	y = []

	p_r = 0.4
	for p in np.arange(0, 1, 0.099):
		y.append((1-(1-(1-p)*(1-p_r))**n)/((1-p)*(1-p_r)))
		x.append(p)

	for p in np.arange(0, 1, 0.099):
		N = find_average_big(p, p_r, n)
		plt.scatter(p, N)

	plt.plot(x, y, label = "p_ret = 0.4")

	x = []
	y = []

	p_r = 0.7
	for p in np.arange(0, 1, 0.099):
		y.append((1-(1-(1-p)*(1-p_r))**n)/((1-p)*(1-p_r)))
		x.append(p)

	for p in np.arange(0, 1, 0.099):
		N = find_average_big(p, p_r, n)
		plt.scatter(p, N)

	plt.plot(x, y, label = "p_ret = 0.7")


	plt.legend()
	plt.show()



if __name__ == '__main__':
 	main() 