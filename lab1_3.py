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

def find_average(p, p_r):
	count = 1
	while(check(p, p_r)):
		count = count + 1
	return count

def find_average_big(p, p_r):
	count_all = 0
	for i in range(0,10000):
		count_all = count_all + find_average(p, p_r)

	result = count_all/10000
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

	print("Enter p_ret: ")
	p_r = float(input())

	x = []
	y = []

	for p in np.arange(0, 1, 0.1):
		y.append(1/((1-p)*(1-p_r)))
		x.append(p)




	for p in np.arange(0, 1, 0.1):
		N = find_average_big(p, p_r)
		plt.scatter(p, N)

	plt.plot(x, y, label = "N(p)")
	plt.xlabel('p')
	plt.ylabel('N')
	plt.title('N(p)')
	plt.legend()
	plt.show()



if __name__ == '__main__':
 	main() 