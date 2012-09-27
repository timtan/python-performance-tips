__author__ = 'tim'
from gevent import spawn, joinall
from gevent import monkey
monkey.patch_all()

def find_max(maximum):
    v = max(range(maximum))
    return v
data = [9999999, 9999999, 9999999] * 3

jobs = [spawn(find_max, maximum) for maximum in data]

joinall(jobs)
