print("Containers:Dictionaries")
d=dict()
d={'cat':'cute','dog':'furry'}
print("Dictionary",d)
print("Is the dictionary has te key 'cat?",'cat' in d)
d['fish']='wet'
print("After adding new entry to 'd' :",d)
print("Get an element monkey :",d.get('monkey','N/A'))
print("Get an element fish :",d.get('fish','N/A'))
del d['fish']
print("After deleting the newly added entry from 'd' :",d)
print("Demo of dictionary comprehension:")
squares={x:x*x for x in range(10)}
print("Squares of integers of range 10:")
for k,v in squares.items():
    print(k,":",v)
