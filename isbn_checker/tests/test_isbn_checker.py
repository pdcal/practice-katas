# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# Extended a little to take 9, 10 & 13 digit ISBNs, a la https://en.wikipedia.org/wiki/International_Standard_Book_Number 
# 20/04/2020 - Phil Calvert 
# Tests for ISBN Checker

import pytest
from isbn_checker.app.isbn_checker import *

isbn_check = IsbnChecker() 

# Input of exit should terminate the program
def test_GivenAnInputOfexit_WhenChoosingISBN_ThenNiceExit():
    assert isbn_check.input_validator("exit")[0] == "soft_exit"
    assert isbn_check.input_validator("exit")[1] == 1

# Should reject input which does not contain 9, 10 or 13 digits
def test_GivenInputNot910or13_WhenSupplyingInput_ThenRejectInput():
    assert isbn_check.input_validator("12345678")[0] == "input_error"
    assert isbn_check.input_validator("12345678901")[0] == "input_error"
    assert isbn_check.input_validator("123456789012")[0] == "input_error"
    assert isbn_check.input_validator("12345678901234")[0] == "input_error"
    assert isbn_check.input_validator("12345678")[1] == 2

# Should accept input which contains 9, 10 or 13 digits
def test_GivenInput910or13_WhenSupplyingInput_ThenAcceptInput():
    assert isbn_check.input_validator("123456789")[0] == "123456789"
    assert isbn_check.input_validator("1234567890")[0] == "1234567890"
    assert isbn_check.input_validator("1234567890123")[0] == "1234567890123"
    assert isbn_check.input_validator("123456789")[1] == 0
    

# Input should reject anything other than numbers, spaces and dashes
def test_GivenInputNumSpaceDash_WhenSupplyingISBN_ThenShouldAccept():
    assert isbn_check.input_validator("12345678!")[0] == "input_error"
    assert isbn_check.input_validator("12345678!")[1] == 2
    assert isbn_check.isbncheck(None)[0] == "input_error"
    assert isbn_check.input_validator(None)[1] == 2
    
# Valid ISBNs with Dashes and spaces should be accepted
def test_GivenInputWithSpacesOrDashes_WhenSupplyingInput_ThenShouldStripThem():
    assert isbn_check.isbncheck("  0-7475-  3269-9")[0] == "Valid ISBN"

# Valid ISBNs should be marked as valid
def test_GivenValidISBN_WhenSupplyingIsbn_ThenShouldReturnValid():
    assert isbn_check.isbncheck("747532699")[0] == "Valid ISBN"
    assert isbn_check.isbncheck("0-7475-3269-9")[0] == "Valid ISBN"
    assert isbn_check.isbncheck("0-7475-3269-9")[1] == True
    assert isbn_check.isbncheck("978-0-306-40615-7")[0] == "Valid ISBN"

# Invalid ISBNs should be marked as invalid
def test_GivenInvalidISBN_WhenSupplyingIsbn_ThenShouldReturnInvalid():
    assert isbn_check.isbncheck("747532698")[0] == "Invalid ISBN"
    assert isbn_check.isbncheck("747532698")[1] == False
    assert isbn_check.isbncheck("9780306406156")[0] == "Invalid ISBN"
