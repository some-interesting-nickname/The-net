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

def find_average(p):
	count = 1
	while(check(p)):
		count = count + 1
	return count

def find_average_big(p):
	count_all = 0
	for i in range(0,100):
		count_all = count_all + find_average(p)

	result = count_all/100
	return result

def main():
	#print("Enter p: ")
	#p = float(input())

	#count_all = 0
	#for i in range(0,1000):
	#	count_all = count_all + find_average(p)

	#result = count_all/1000
	#print("Average number of requests:" + str(result))

	x = []
	y = []

	for p in np.arange(0, 1, 0.1):
		y.append( 1/(1-p))
		x.append(p)

	for p in np.arange(0, 1, 0.1):
		N = find_average_big(p)
		plt.scatter(p, N)

	plt.plot(x, y, label = "N(p)")
	plt.xlabel('p')
	plt.ylabel('N')
	plt.title('N(p)')
	plt.legend()
	plt.show()



if __name__ == '__main__':
 	main() 