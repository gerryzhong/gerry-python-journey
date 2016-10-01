import threading
import random
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker():
	""" Thread worker function"""
	pause = random.randint(1,5)
	logging.debug("sleep %s " % pause)
	time.sleep(pause)
	logging.debug("ending")
	
for i in range(1,3):
	thread = threading.Thread(target = worker)
	thread.setDaemon(True)
	thread.start()
	
main_thread = threading.currentThread()
for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug("Joining %s" % t.getName())
	t.join()
	
	