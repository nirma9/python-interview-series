#map
nums = [1,2,3,4]
sq = list(map(lambda x :x*x, nums))
print(sq)

#filter
nums = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x : x % 2 == 0, nums))
print(evens)

#reduce
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x,y : x*y,nums)
print(product)

#map + filter+ reduce
from functools import reduce

nums = [1,2,3,4,5,6,7]
result = reduce(
               lambda x,y : x+y, 
               filter(
                              lambda x: x% 2 == 0,
                              map(lambda x :x*x , nums)
               )
)
print(result)