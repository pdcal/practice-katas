# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# Extended a little to take 9, 10 & 13 digit ISBNs, a la https://en.wikipedia.org/wiki/International_Standard_Book_Number 
# 21/04/2020 - Phil Calvert 
# Tests for ISBN Generator

from isbn_checker.app.isbn_generator import *
from isbn_checker.app.isbn_checker import *

isbn_generator = IsbnGenerator()
isbn_checker = IsbnChecker()

def test_GivenValidInput_WhenInputting_ThenAcceptInput():
    assert isbn_generator.input_validator("a")[0] == "a"
    assert isbn_generator.input_validator("B")[0] == "b"

def test_GivenInvalidInput_WhenChoosingIsbnType_ThenReject():
    assert isbn_generator.input_validator(None)[0] == "input_error"
    assert isbn_generator.input_validator("c")[0] == "input_error"
    assert isbn_generator.input_validator("c")[1] == 1

def test_GivenInput_WhenChoosingInput_ThenCorrectIsbnOutput():
    assert isbn_checker.isbncheck(isbn_generator.isbn_generator("a"))[1] == True
    assert isbn_checker.isbncheck(isbn_generator.isbn_generator("b"))[1] == True
    assert len(isbn_generator.isbn_generator("a")) == 10
    assert len(isbn_generator.isbn_generator("b")) == 13
