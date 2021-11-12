import numpy as np
import pandas as pd

givenAddresses = ['5' '11', '4', '11', 'C', 'D', 'D', 'C', 'D', '12']
addresses = list(map(lambda x:int(str(x),16), givenAddresses.copy()))
addresses = np.array(addresses)
num_of_cache_sets = 4
# K-way
k = 2

#size of block
offset = 4

Bx = addresses//offset

# Bx = addresses


cache = np.full((num_of_cache_sets, k), np.inf)

current_size_of_sets = np.full((num_of_cache_sets), 0)

print()
num_of_hits=0
result_of_req=[]
for memory_block_address in Bx:

    cache_index = memory_block_address%num_of_cache_sets

    res = ""
    print("--------------------------")
    if memory_block_address in cache[cache_index]:
        #most be changed
        index_of_mem_block_in_cache = (np.where( cache[cache_index] == memory_block_address))[0][0]
        temp = current_size_of_sets[cache_index]
        #move requested address to queue
        cache[cache_index, index_of_mem_block_in_cache:(temp-1)] = cache[cache_index, (index_of_mem_block_in_cache+1):temp] 
        cache[cache_index, temp-1] = memory_block_address
        res = "hit"
        result_of_req.append("hit")
        num_of_hits+=1
    else:
        if current_size_of_sets[cache_index] == k:
            #replacement
            cache[cache_index, 0:k-1] = cache[cache_index, 1:]
            
            cache[cache_index, k-1] = memory_block_address

        else:
            temp = current_size_of_sets[cache_index]
            cache[cache_index, temp] = memory_block_address
            
            current_size_of_sets[cache_index]+=1
        res= "miss"
        result_of_req.append("miss")


    print("cache rep\n",cache[cache_index])
    # print("cache rep\n",cache)
    print("{0} {1}  cache_index: {2}".format(res ,memory_block_address, cache_index))
    print()




data = {
  "given Add": givenAddresses,
  "Decimal Add": addresses,
  "M.M Block Add": Bx,
  "Cache Block Add": Bx%num_of_cache_sets,
  "Hits": result_of_req
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.T) 

print("hit rate: ", "{}/{}".format(num_of_hits, len(addresses)))
print("hit rate: ", (num_of_hits/len(addresses))*100,"%")