It seems like you want to know about properties of arrays and some operations that can be performed on arrays in Python. Here's the information you provided in a more readable format:

## Properties of Arrays
1. Each array element is of the same data type and size. For example, in an array of integers with the int data type, each element occupies 4 bytes.

2. Elements of the array are stored in contiguous memory locations.

## Operations on Arrays in Python
Here are some common operations that can be performed on arrays in Python:

- `append()`: This method is used to add a value to the end of the array.

- `insert()`: It allows you to insert a value at a specific position in the array.

- `pop()`: Removes and returns the last element of the array.

- `remove()`: Removes the first occurrence of a specified value from the array.

- `index()`: Returns the index of the first occurrence of a specified value.

- `reverse()`: Reverses the order of elements in the array.

## Creating an Array in Python
You can create an array in Python using the `array` function, which allows you to specify the data type and provide a list of values. Here are some common data types and their respective type codes:

- 'b': Signed char (int), minimum size in bytes: 1
- 'B': Unsigned char (int), minimum size in bytes: 1
- 'u': Py_UNICODE (Unicode character), minimum size in bytes: 2
- 'h': Signed short (int), minimum size in bytes: 2
- 'H': Unsigned short (int), minimum size in bytes: 2
- 'i': Signed int (int), minimum size in bytes: 2
- 'I': Unsigned int (int), minimum size in bytes: 2
- 'l': Signed long (int), minimum size in bytes: 4
- 'L': Unsigned long (int), minimum size in bytes: 4
- 'q': Signed long long (int), minimum size in bytes: 8
- 'Q': Unsigned long long (int), minimum size in bytes: 8
- 'f': Float (float), minimum size in bytes: 4
- 'd': Double (float), minimum size in bytes: 8

To create an array, you can use the `array` function like this:

```python
from array import array

my_array = array('i', [1, 2, 3, 4, 5])  # Creating an array of integers
```

You can replace 'i' with the appropriate type code for your desired data type.

The `append()` method is used to add elements to the end of the array, as demonstrated below:

```python
my_array.append(6)  # Adds the value 6 to the end of the array
```

I hope this information is helpful for your understanding of arrays and array operations in Python.