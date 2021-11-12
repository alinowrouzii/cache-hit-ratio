



import numpy as np
import pandas as pd

givenAddresses = ['5' '11', '4', '11', 'C', 'D', 'D', 'C', 'D', '12']
addresses = list(map(lambda x:int(str(x),16), givenAddresses.copy()))
addresses = np.array(addresses)
num_of_cache_sets = 1
k = 5

#size of block
# offset = 

# Bx = addresses//offset

Bx = addresses


cache = np.full((num_of_cache_sets, k), np.inf)

current_size_of_sets = np.full((num_of_cache_sets), 0)

print()
num_of_hits=0
result_of_req=[]
for idx, memory_block_address in enumerate(Bx):

    cache_index = memory_block_address%num_of_cache_sets

    res = ""
    print("----------------------")
    if memory_block_address in cache[cache_index]:
        res = "hit"
        result_of_req.append("hit")
        num_of_hits+=1

    else:
        #implement the fifo policy
        if current_size_of_sets[cache_index] == k:
            #shift array and remove first element
            cache[cache_index, 0:k-1] = cache[cache_index, 1:]
            cache[cache_index, k-1] = memory_block_address

        else:
            temp = current_size_of_sets[cache_index]
            cache[cache_index, temp] = memory_block_address

            current_size_of_sets[cache_index]+=1
        res= "miss"
        result_of_req.append("miss")


    print("cache rep\n",cache[cache_index])
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

