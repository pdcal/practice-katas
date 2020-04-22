# ISBN Generator - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# 21/04/2020 - Phil Calvert 
# Interactive implementation of ISBN generator

from random import randint

class IsbnGenerator:
    def isbn_generator(self, isbn_type):
        isbn_to_generate = self.input_validator(isbn_type)[0]
        generated_isbn = self.__generate_isbn(isbn_to_generate)
        while len(generated_isbn) == 11:
            generated_isbn = self.__generate_isbn(isbn_to_generate)
        return generated_isbn

    def input_validator(self, isbn_input):
        accepted_input = "ab"
        if isbn_input is None: return "input_error", 1
        if isbn_input.lower() not in accepted_input: return "input_error", 1
        else: return isbn_input.lower(), 0

    def __generate_isbn(self, isbn_type):
        if isbn_type == "a": 
            isbn_seed = randint(100000000,999999999)
            isbn_seed = str(isbn_seed)
            running_total = 0
            multiplier = 10
            
            for i in range(9):
                running_total = running_total + (int(isbn_seed[i]) * multiplier)
                multiplier = multiplier - 1

            check_digit = (11 - (running_total % 11)) % 11

            generated_isbn = str(isbn_seed) + str(check_digit)
        else:
            isbn_seed = randint(100000000000,999999999999)
            isbn_seed = str(isbn_seed)
            running_total = 0

            for i in range(12):
                multiplier = 1
                if i > 0 and i % 2 != 0: multiplier = 3 
                running_total = running_total + (int(isbn_seed[i]) * multiplier)

            check_digit = (10 - (running_total % 10)) % 10
            generated_isbn = isbn_seed + str(check_digit)

        return generated_isbn

