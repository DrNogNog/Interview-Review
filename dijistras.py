# import reduce
# arr1 = [1,2,3,4,5]
# arr2 = map(lambda x: 2 * x, arr1)
# print(arr2)

# arr3 = reduce(lambda x,y: x+y, arr1)

#lambda is an anonymous function
#bloomfilters - a guesstimate filter
#hyperloglog- approximates the number of unique elements
#Diffie-Hellman algorithm

scifi_a = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Douglas Adams"]
scifi_a.sort(key=lambda x: x.split(" ")[0].lower())
print(scifi_a)

#dijistras finds the shortest path by means of weight on edges
