import time

start = time.time()
def square(num):
    return num**2
    
squares = []
for i in range(1000000):
    squares.append(square(i))
end = time.time()

print ("Time Elapsed (Funtion Call):{}".format((end-start)))

start = time.time()
def sqaure_1(num):
    squares = []
    for i in range(1000000):
        squares.append(i**2)
    return squares
sqaure_1(1000000)
end = time.time()
print ("Time Elapsed (Iterative Approach):{}".format((end-start)))
