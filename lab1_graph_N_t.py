import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

def check(p):
	x = np.random.uniform(0,1)

	if(x > p):
		return 1
	else:
		return 0

def send(p, t, L):
	max_time = 100
	count = 0
	happy_count = 0
	buffer = np.empty(0, dtype=int)
	last_recieved = 0
	not_recieved_arr = np.zeros(t+1, dtype=int)
	message_again = 0

	for time in range(0, max_time):
		time_moment = time % (t + 1)
		if(not_recieved_arr[time_moment] != 0):
			message_again += 1
			if(np.random.uniform(0,1) > p):
				if(not_recieved_arr[time_moment] == (last_recieved + 1)):
					not_recieved_arr[time_moment] = 0
					last_recieved += 1
					while (buffer.size > 0):
						if(buffer[0] == (last_recieved + 1)):
							last_recieved += 1
							buffer = np.delete(buffer, 0)
						else:
							break
				else:
					if(buffer.size < L):
						buffer = np.append(buffer, not_recieved_arr[time_moment])
						buffer = np.sort(buffer)
						not_recieved_arr[time_moment] = 0
		else:
			count += 1
			if(np.random.uniform(0,1) > p):
				if(count == (last_recieved + 1)):
					last_recieved += 1
					while (buffer.size > 0):
						if(buffer[0] == (last_recieved + 1)):
							last_recieved += 1
							buffer = np.delete(buffer, 0)
						else:
							break
				else:
					if(buffer.size < L):
						buffer = np.append(buffer, count)
						buffer = np.sort(buffer)
					else:
						not_recieved_arr[time_moment] = count
			else:
				not_recieved_arr[time_moment] = count

	return message_again


def find_average(p, t, L):
	count = 0
	for i in range(0,1000):
		count = count + send(p, t, L)

	result = count/1000
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

	print("Enter p: ")
	p = float(input())

	print("Enter L:")
	L = int(input())

	#print("Enter p:")
	#p = float(input())

	#number = 10
	#send(p, t, L, number)

	#print(f"mes_number = {mes_number}")
	#print(f"time = {time}")
	#print(f"N(t) = {mes_number/time}")
	
	x = []
	y = []

	#for p in np.arange(0, 1, 0.1):
	#	y.append((1-p)/(1+t))
	#	x.append(p)


	for t in range(1, 100):
		N = find_average(p, t, L)
		y.append(N)
		x.append(t)
		#plt.scatter(p, N)

	plt.plot(x, y, label = "N(t,p = const)")


	plt.xlabel('t')
	plt.ylabel('N')
	plt.title('N(t,p)')
	plt.legend()
	plt.show()

if __name__ == '__main__':
 	main() 