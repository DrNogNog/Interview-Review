arr1 = [1,2,3,4,5]
arr2 = map(lambda x: 2 * x, arr1)
print(arr2)

arr3 = reduce(lambda x,y: x+y, arr1)

#bloomfilters - a guesstimate filter
#hyperloglog- approximates the number of unique elements
#Diffie-Hellman algorithm
