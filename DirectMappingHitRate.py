
import numpy as np
import pandas as pd

givenAddresses = ['5' '11', '4', '11', 'C', 'D', 'D', 'C', 'D', '12']
addresses = list(map(lambda x: int(x, 16), givenAddresses.copy()))
addresses = np.array(addresses)
num_of_cache_blocks = 8

# size of block
# offset = 4

# Bx = addresses//offset

Bx = addresses


cache = np.full((num_of_cache_blocks), np.inf)
num_of_hits = 0
result_of_req = []
for memory_block_address in Bx:
    cache_index = memory_block_address % num_of_cache_blocks
    if cache[cache_index] == memory_block_address:
        result_of_req.append("hit")
        num_of_hits += 1
    else:
        cache[cache_index] = memory_block_address
        result_of_req.append("miss")


data = {
    "given Add": givenAddresses,
    "Decimal Add": addresses,
    "M.M Block Add": Bx,
    "Cache Block Add": Bx % num_of_cache_blocks,
    "Hits": result_of_req
}

# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.T)

print("hit rate: ", "{}/{}".format(num_of_hits, len(addresses)))
print("hit rate: ", (num_of_hits/len(addresses))*100, "%")
