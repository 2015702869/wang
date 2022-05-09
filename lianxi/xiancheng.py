import threading
import time
class word_one(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        if l1.acquire():
            print(1)
            l3.release()
class word_two(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        if l2.acquire():
            print(2)
            l1.release()
class word_fwo(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        if l3.acquire():
            print(3)
            l2.release()

t1 = word_one()
t2 = word_two()
t3 = word_fwo()

l1 = threading.Lock()
l2 = threading.Lock()
l3 = threading.Lock()

l2.acquire()
l3.acquire()

t1.start()
t2.start()
t3.start()