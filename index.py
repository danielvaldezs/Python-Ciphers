#!/usr/bin/env python3
import collections
import string

my_string = "Hello, World!"

def caesar(rotate_string, number_to_rotate_by):
      upper = collections.deque(string.ascii_uppercase) 
      lower = collections.deque(string.ascii_lowercase)

      upper.rotate(number_to_rotate_by)
      lower.rotate(number_to_rotate_by)
      

      upper = ''.join(list(upper))
      lower = ''.join(list(lower)) 

      return rotate_string.translate(str.maketrans(string.ascii_uppercase)).translate(str.maketrans(string.ascii_lowercase))


print(caesar(my_string, 1))
