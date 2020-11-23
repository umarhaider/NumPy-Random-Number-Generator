import time
import random
import numpy as np


print("  _   _                 _____         _   _                   _____ _      _             \n | \ | |               |  __ \       | \ | |                 |  __ (_)    | |            \n |  \| |_   _ _ __ ___ | |__) |   _  |  \| |_   _ _ __ ___   | |__) |  ___| | _____ _ __ \n | . ` | | | | '_ ` _ \|  ___/ | | | | . ` | | | | '_ ` _ \  |  ___/ |/ __| |/ / _ \ '__|\n | |\  | |_| | | | | | | |   | |_| | | |\  | |_| | | | | | | | |   | | (__|   <  __/ |   \n |_| \_|\__,_|_| |_| |_|_|    \__, | |_| \_|\__,_|_| |_| |_| |_|   |_|\___|_|\_\___|_|   \n                               __/ |                                                     \n                              |___/                                                      \n")

limit = input('Amount of numbers to generate?: ')
printyn = input('Want to print the list at the end? Y/N: ')
rndnum = random.randint(0, int(limit)-1) # - 1 because it gives an error of getting index if it generates number thats same as the limit as indexing starts from 0

nums = []

start = time.perf_counter()


start1 = time.perf_counter()

nums = np.random.randint(0, int(limit), int(limit))

min  = nums.min()

end1 = time.perf_counter()
elapsed_numpy = end1 - start1

print(f'Number: {nums[int(rndnum)]}')
print(f'This took: {elapsed_numpy}s')
if printyn == 'Y' or printyn == 'y':
    print(f'LIST: \n {nums}')


