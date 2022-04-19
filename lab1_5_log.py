import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

def send(p):
	x = np.random.uniform(0,1)

	if(x > p):
		return 0
	else:
		return 1

def check(p, t, number):
	count = 1
	time =  0
	while count < number:		

		print(f"Send message {count}")
		if(send(p)):
			print(f"Failed to recieve {count}")
			time += 1 + t
			for j in range(1,t + 1):
				print(f"Send message {count + j}")
				print(f"Deleted message {count + j}")
		else:
			print(f"Recieved {count}")
			time += 1
			count += 1	

		
	return count, time

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

	print("Enter t: ")
	t = int(input())

	print("Enter p: ")
	p = float((input()))

	number = 4
	check(p, t, number)

	#print(f"mes_number = {mes_number}")
	#print(f"time = {time}")
	#print(f"N(t) = {mes_number/time}")
	'''
	x = []
	y = []

	for p in np.arange(0, 1, 0.1):
		y.append((1-p)/(1+p*t))
		x.append(p)


	for p in np.arange(0, 1, 0.1):
		mes_number, time = check(p, t)
		N = mes_number/time
		plt.scatter(p, N)

	plt.plot(x, y, label = "N(t,p)")
	plt.xlabel('p')
	plt.ylabel('N')
	plt.title('N(t,p)')
	plt.legend()
	plt.show()
	'''
if __name__ == '__main__':
 	main() 