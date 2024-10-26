import time
import tracemalloc

tracemalloc.start()

lst = [50] * 50000 + [100] * 50000
start_time = time.time()

for i in range(50000):
    lst.remove(100)
for i in range(50000):
    lst.remove(50)

end_time = time.time()

current, peak = tracemalloc.get_traced_memory()

print(f"Time taken: {end_time - start_time:.5f} sec")
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()


