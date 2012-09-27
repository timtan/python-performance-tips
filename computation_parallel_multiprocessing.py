__author__ = 'tim'

import multiprocessing
def find_max(maximum):
    v = max(range(maximum))
    return v
data = [9999999, 9999999, 9999999] * 3
pool = multiprocessing.Pool(2)

print pool.map(find_max, data)
pool.close()
