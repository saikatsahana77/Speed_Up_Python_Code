import time 

start = time.time()
sorted_list =[]
numbers = list(range(10000000))
for x in numbers:
    if x % 2 == 0:
        sorted_list.append(x**2)
end = time.time() 
print ("Elapsed time (Using for loop and new list): {}".format((end-start)))

start = time.time()
numbers = []
for x in range(10000000):
    if x % 2 == 0: 
        numbers.append(x**2)
end = time.time()
print ("Elapsed time (Using an iterator): {}".format((end-start)))

start = time.time()
numbers = [x**2 for x in range(10000000) if x % 2 == 0]
end = time.time()
print ("Elapsed time (list comprehension): {}".format((end-start)))

