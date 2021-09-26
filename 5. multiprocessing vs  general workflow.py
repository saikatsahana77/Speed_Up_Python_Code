import time

start = time.time()
import multiprocessing
from multiprocessing import Process

def test():
    return "Running"

def square(n):
    ar = []
    for i in range(0,n):
        ar.append(i**2)
    return ar

def cube(n):
    ar = []
    for i in range(0,n):
        ar.append(i**3)
    return ar

p1=Process(target=square,args=(10000000,))
p2=Process(target=cube,args=(100000000,))
p3=Process(target=test)
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()
end= time.time()
print ("Elapsed time (using multiprocessing):", (end-start))


start = time.time()
test()
square(10000000)
cube(10000000)
end= time.time()
print ("Elapsed time (without multiprocessing):", (end-start))