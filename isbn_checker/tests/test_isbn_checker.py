# ISBN Check - Kata for https://github.com/davidwhitney/CodeDojos/tree/master/ISBNValidator 
# Extended a little to take 9, 10 & 13 digit ISBNs, a la https://en.wikipedia.org/wiki/International_Standard_Book_Number 
# 20/04/2020 - Phil Calvert 
# Tests for ISBN Checker

import pytest
from isbn_checker.app.isbn_checker import *

isbn_check = IsbnChecker() 

# Input of exit should terminate the program
def test_GivenAnInputOfexit_WhenChoosingISBN_ThenNiceExit():
    assert isbn_check.isbncheck("exit") == "soft_exit"

# Should reject input which does not contain 9, 10 or 13 digits
def test_GivenInputNot910or13_WhenSupplyingInput_ThenRejectInput():
    assert isbn_check.isbncheck("12345678") == "input_error"
    assert isbn_check.isbncheck("12345678901") == "input_error"
    assert isbn_check.isbncheck("123456789012") == "input_error"
    assert isbn_check.isbncheck("12345678901234") == "input_error"

# Should accept input which contains 9, 10 or 13 digits
def test_GivenInput910or13_WhenSupplyingInput_ThenAcceptInput():
    assert isbn_check.isbncheck("123456789") == "0123456789"
    assert isbn_check.isbncheck("1234567890") == "1234567890"
    assert isbn_check.isbncheck("1234567890123") == "1234567890123"

# Input should reject anything other than numbers, spaces and dashes
def test_GivenInputNumSpaceDash_WhenSupplyingISBN_ThenShouldAccept():
    assert isbn_check.isbncheck("12345678!") == "input_error"
    assert isbn_check.isbncheck(None) == "input_error"
    
# Dashes and spaces should be stripped from the input
def test_GivenInputWithSpacesOrDashes_WhenSupplyingInput_ThenShouldStripThem():
    assert isbn_check.isbncheck("  0-7475-  3269-9") == "0747532699"

# 9 digit numbers should be converted to ten digit by adding a 0 to the start 
def test_Given9DigitBSN_WhenSupplyingIsbn_ThenZeroShouldPrepend():
    assert isbn_check.isbncheck("123456789") == "0123456789"

# 10 digit ISBNs should be validated per the check supplied

# 0-7475-3269-9 should be valid

# 0-7475-3269-8 should be invalid

# 13 digit ISBNs should be validated per the researched check

# Input other than numbers, spaces and dashes should ask the user to re-input (inc. None)
