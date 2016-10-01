import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
def worker(counter,delay):
	while counter:
		logging.debug('%s starting' % threading.currentThread().getName())
		time.sleep(delay)
		logging.debug('%s exiting' % threading.currentThread().getName())
		counter -= 1

def my_service(counter,delay):
	while counter:
		logging.debug('%s starting' % threading.currentThread().getName())
		time.sleep(delay)
		logging.debug('%s exiting' % threading.currentThread().getName())
		counter -= 1
	
w = threading.Thread(name = "worker",target = worker,args = (3,2))
s = threading.Thread(name = "my_service",target = my_service,args = (4,3))
w1 = threading.Thread(target = worker,args = (5,1))

w.start()
s.start()
w1.start()
