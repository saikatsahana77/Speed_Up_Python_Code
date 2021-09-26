import numpy as np
import time

def builtin_sum():
  return sum(range(10000000))

def numpy_sum():
  return np.sum(np.arange(0,10000000))

start = time.time()
numpy_sum()
end= time.time()
print ("Time Elapsed (Numpy Sum): {}".format((end-start)))

start = time.time()
builtin_sum()
end= time.time()
print ("Time Elapsed (Builtin Sum in python): {}".format((end-start)))

