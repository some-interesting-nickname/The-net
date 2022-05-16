import random
import numpy as np
import matplotlib.pyplot as plt
import threading

random.seed()

def send(p, t, L):
	max_time = 30
	count = 0
	happy_count = 0
	buffer = np.empty(0, dtype=int)
	last_recieved = 0
	not_recieved_arr = np.zeros(t+1, dtype=int)

	for time in range(0, max_time):
		time_moment = time % (t + 1)
		if(not_recieved_arr[time_moment] != 0):
			print(f"Send message {not_recieved_arr[time_moment]}")
			if(np.random.uniform(0,1) > p):
				print(f"Message {not_recieved_arr[time_moment]} received")
				if(not_recieved_arr[time_moment] == (last_recieved + 1)):
					print(f"Message {not_recieved_arr[time_moment]} go up")
					not_recieved_arr[time_moment] = 0
					last_recieved += 1
					while (buffer.size > 0):
						if(buffer[0] == (last_recieved + 1)):
							last_recieved += 1
							print(f"Message {buffer[0]} popped out of buffer")
							buffer = np.delete(buffer, 0)
						else:
							break
				else:
					if( buffer.size < L):
						print(f"Message {not_recieved_arr[time_moment]} added to buffer")
						buffer = np.append(buffer, not_recieved_arr[time_moment])
						buffer = np.sort(buffer)
						not_recieved_arr[time_moment] = 0
					else:
						print(f"Message {not_recieved_arr[time_moment]} deleted")
			else:
				print(f"Message {not_recieved_arr[time_moment]} not received")
		else:
			count += 1
			print(f"Send message {count}")
			if(np.random.uniform(0,1) > p):
				print(f"Message {count} received")
				if(count == (last_recieved + 1)):
					print(f"Message {count} go up")
					last_recieved += 1
					while (buffer.size > 0):
						if(buffer[0] == (last_recieved + 1)):
							print(f"Message {buffer[0]} popped out of buffer")
							last_recieved += 1
							buffer = np.delete(buffer, 0)
						else:
							break
				else:
					if(buffer.size < L):
						print(f"Message {count} added to buffer")
						buffer = np.append(buffer, count)
						buffer = np.sort(buffer)
					else:
						print(f"Message {count} deleted")
						not_recieved_arr[time_moment] = count
			else:
				print(f"Message {count} not received")
				not_recieved_arr[time_moment] = count

	return last_recieved, max_time


def main():


	print("Enter p:")
	p = float(input())

	print("Enter t:")
	t = int(input())

	print("Enter L:")
	L = int(input())

	send(p, t, L)


if __name__ == '__main__':
 	main() 