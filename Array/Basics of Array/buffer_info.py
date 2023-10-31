# importing "array" for array operations
import array
	
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

# using buffer_info() to print buffer info. of array
print ("The buffer info. of array is : ")
print (arr.buffer_info())
