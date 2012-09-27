__author__ = 'tim'

def find_max(maximum):
    v = max(range(maximum))
    print v

for maximum in [9999999, 9999999, 9999999] * 3:
    find_max(maximum)