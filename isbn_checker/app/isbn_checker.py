# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# 20/04/2020 - Phil Calvert 
# Class for ISBN Checker

class IsbnChecker:

    def isbncheck(self, isbn_to_check):
        input_check = self.__input_validator(isbn_to_check)
        validated_input = input_check[0]
        error_state = input_check[1]
        if (error_state > 0):
            return validated_input
        else:
            isbn_check = self.__isbn_validator(validated_input)
            isbn_result = isbn_check[0]
            error_state = isbn_result[1]
        return isbn_result

    def __input_validator(self, isbn_to_check):
        valid_isbn_lengths = [9, 10, 13]
        if (isbn_to_check == "exit"):
            return "soft_exit", 1
        else:
            if (isbn_to_check is None):
                return "input_error", 2
            validated_input = isbn_to_check.replace(" ","").replace("-","")
            if ((len(validated_input) not in valid_isbn_lengths) or (validated_input.isnumeric() is False)):
                return "input_error", 2
        return validated_input, 0

    def __isbn_validator(self, validated_input):
        isbn_type = len(validated_input)
        if (isbn_type < 13):
            if(isbn_type < 10):
                validated_isbn = "0" + validated_input
            else: 
                validated_isbn = validated_input
        else: 
            validated_isbn = validated_input

        return validated_isbn, 0
