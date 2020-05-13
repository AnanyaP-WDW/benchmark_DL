import numpy as np
import time
# checking time for vector multiplication
a = np.random.rand(1000000)
b = np.random.rand(1000000)
t0 = time.time()
c = np.dot(a,b)
t1 = time.time()
print("Vectorized version" +" *** " + str(1000*(t1-t0)) + " ms")

 # checking time for "for" loop

t0 = time.time()
for i in range(1000000):
    c += a[i]*b[i]
t1 = time.time()
print("for loop version"+ " ***" + str(1000*(t1-t0)) + " ms")
