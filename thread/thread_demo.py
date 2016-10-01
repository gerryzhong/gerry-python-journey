from threading import Thread
import time

def worker(thread_id,delay,counter):
	""" The worker function"""
	while counter:
		print "thread-%s is working" % thread_id
		time.sleep(delay)
		counter -= 1
	
def main():
	for i in range(1,3):
		thread = Thread(target = worker,args = (i,i,i+3))
		thread.start()

if __name__ == "__main__":
	main()