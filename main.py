#programa Principal
import math_operations
from string_utils import capitalize, reverse_string, count



print(math_operations.sum(5, 3)) # Output: 8
print(math_operations.subtract(10, 4)) # Output: 6
print(math_operations.multiply(2, 7)) # Output: 14      
print(math_operations.divide(15, 0)) # Output: 5.0

print(capitalize("hello")) # Output: "Hello"
print(reverse_string("hello")) # Output: "olleh"        
print(count("hello")) # Output: 5