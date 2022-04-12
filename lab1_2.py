import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

def check(p):
	x = np.random.uniform(0,1)

	if(x > p):
		return 0
	else:
		return 1

def find_average(p, n):
	count = 1
	while(check(p) and (count < n)):
		count = count + 1
	return count

def find_average_big(p, n):
	count_all = 0
	for i in range(0,1000):
		count_all = count_all + find_average(p, n)

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

	print("Enter n: ")
	n = float(input())

	x = []
	y = []

	for p in np.arange(0, 1, 0.099):
		y.append((1-p**n)/(1-p))
		x.append(p)

	for p in np.arange(0, 1, 0.099):
		N = find_average_big(p, n)
		plt.scatter(p, N)

	plt.plot(x, y, label = "N(p)")
	plt.xlabel('p')
	plt.ylabel('N')
	plt.title('N(p)')
	plt.legend()
	plt.show()



if __name__ == '__main__':
 	main() 