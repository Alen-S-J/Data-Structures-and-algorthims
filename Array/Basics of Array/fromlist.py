# importing "array" for array operations
import array
	
# initializing array with array values
arr = array.array('i',[1, 2, 3, 1, 2, 5]) 
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)

# printing the modified array
print ("The modified array is : ",end="")
for i in range (0,9):
	print (arr[i],end=" ")
