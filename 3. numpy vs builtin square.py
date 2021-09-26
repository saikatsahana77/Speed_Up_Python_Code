import time
import numpy as np

start = time.time()
python_list = [i for i in range(1000000)]

python_list = [i**2 for i in python_list]
end= time.time()
print ("Elapsed time (without numpy):", (end-start))

start = time.time()
numpy_array = np.array([i for i in range(1000000)])

numpy_array = np.square(numpy_array)
end= time.time()
print ("Elapsed time (with numpy):", (end-start))
