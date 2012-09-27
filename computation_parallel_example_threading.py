__author__ = 'tim'
from threading import Thread
import Queue

queue = Queue.Queue()


def find_max():
    while True:
        maximum = queue.get()
        v = max(range(maximum))
        print v
        queue.task_done()

data = [9999999, 9999999, 9999999] * 3
for d in data:
    t = Thread(target=find_max)
    t.setDaemon(True)
    t.start()

for maximum in data:
    queue.put(d)
queue.join()
print 'finish'

