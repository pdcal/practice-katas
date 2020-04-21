# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# 20/04/2020 - Phil Calvert 
# Interactive implementation of ISBN checker. 

from isbn_checker import IsbnChecker

isbn_input = input("Please enter an ISBN to validate: ")

isbn_checker = IsbnChecker()

isbn_checker_output = isbn_checker.isbncheck(isbn_input)

print(isbn_checker_output)
