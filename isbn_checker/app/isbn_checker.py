# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# 20/04/2020 - Phil Calvert 
# Class for ISBN Checker

class IsbnChecker:

    def isbncheck(self, isbn_to_check):
        input_check = self.input_validator(isbn_to_check)
        validated_input = input_check[0]
        input_error_state = input_check[1]
        if (input_error_state > 0):
            return validated_input, input_error_state
        isbn_check = self.__isbn_validator(validated_input)
        return isbn_check[0], isbn_check[1]

    def input_validator(self, isbn_to_check):
        valid_isbn_lengths = [9, 10, 13]
        if (isbn_to_check == "exit"):
            return "soft_exit", 1
        else:
            if (isbn_to_check is None): return "input_error", 2
            validated_input = str(isbn_to_check).replace(" ","").replace("-","")
            if ((len(validated_input) not in valid_isbn_lengths) or (validated_input.isnumeric() is False)):
                return "input_error", 2
        return validated_input, 0

    def __isbn_validator(self, validated_input):
        isbn_type = len(validated_input)
        isbn_to_check = validated_input
        if (isbn_type < 13):
            if(isbn_type < 10): isbn_to_check = "0" + validated_input
    
            running_total = 0
            multiplier = 10
            
            for i in range(10):
                running_total = running_total + (int(isbn_to_check[i]) * multiplier)
                multiplier = multiplier - 1

            if ((running_total % 11 == 0)): validated_isbn = "Valid ISBN"
            else: return "Invalid ISBN", False
        else: # Stuff to do with 13 char isbn

            running_total = 0

            for i in range(13):
                multiplier = 1
                if i > 0 and i % 2 != 0: multiplier = 3 
                running_total = running_total + (int(isbn_to_check[i]) * multiplier)

            if running_total % 10 == 0: validated_isbn = "Valid ISBN"
            else: return "Invalid ISBN", False
        return validated_isbn, True
