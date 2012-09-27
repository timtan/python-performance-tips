__author__ = 'tim'
from threading import Thread
import Queue

queue = Queue.Queue()


def find_max(value):

    v = max(range(value))
    print v

def find_max_thread():
    while True:
        value = queue.get()
        find_max(value)
        queue.task_done()

data = [9999999, 9999999, 9999999] * 3

for maximum in data:
    queue.put(maximum)

for maximum in data:
    t = Thread(target=find_max_thread)
    t.setDaemon(True)
    t.start()

queue.join()
print 'finish'

