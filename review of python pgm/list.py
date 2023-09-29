print("Containers:Lists")
nums=list(range(5))
print("list 'nums' contains:",nums)
nums[4]="abc"
print("List can contain elements of different types.Example:",nums)
nums.append("xyz")
print("nums after inserting new element at the end:")
print("Sublists:")
print("A slice from index 2 to 4:",nums[2:4])
print("A slice from index 2 to the end:",nums[2:])
print("A slice from the start to index 2:",nums[:2])
print("A slice of the whole list:",nums[:])
nums[4:]=[8,9] #Assign a new sublist to a slice
print("After assigning a new sublist to 'nums' :")
for idx,i in enumerate(nums):
    print('%d:%s' % (idx+1,i))
even_squares=[x**2 for x in nums if x%2==0]
print("List of squares of even numbers from 'nums' :",even_squares)

