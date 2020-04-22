# ISBN Generate - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# 22/04/2020 - Phil Calvert 
# Interactive implementation of ISBN Generator

from isbn_generator import *

isbn_input = input("Enter 'a' for a 10 digit ISBN or 'b' for a 13 digit ISBN: ")

isbn_generate = IsbnGenerator()

isbn_generated = isbn_generate.isbn_generator(isbn_input)

print("Your artisinal ISBN is: " + isbn_generated)