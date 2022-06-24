#!/usr/bin/python3

import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print ('String ' + self.name)
		print_time(self.name, self.counter, 5)
		print ('Exiting ' + self.name)

def print_time(thread_name, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print ('%s : %s' % (thread_name, time.ctime(time.time())))
		counter -= 1
print ('new thread1 thread2 ')
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

print ('Start thread1 thread2')
thread1.start()
thread2.start()

print ('Join thread1 thread2')
thread1.join()
thread2.join()

print ('Exiting Main Thread!')

