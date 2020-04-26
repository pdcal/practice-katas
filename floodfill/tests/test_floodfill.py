# Floodfill kata, response to https://github.com/davidwhitney/CodeDojos/tree/master/FloodFill
# 24/04/20 - Phil Calvert
# Floodfill Tests

from floodfill.app.floodfill import *
import pytest

floodfill = FloodFill()
accepted_characters = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYOPZXCVBNM1234567890@,"

@pytest.mark.parametrize("character", accepted_characters)
def test_GivenAnyValidCharacter_WhenMapper_ThenFilledWithChar(character):
    grid = ["#    #"]
    result = floodfill.mapper(grid, 1, 0, character) 
    expected = ["#    #".replace(' ', character)]
    assert result == expected

def test_GivenInvalidCharacter_WhenMapper_ThenReject():
    grid = ["#....#"]
    result = floodfill.mapper(grid, 1, 0, "~") 
    expected = "Please supply a valid character"
    assert result == expected    

def test_GivenGridWithoutBorders_WhenMapper_ThenStillWork():
    grid = ["...."]
    result = floodfill.mapper(grid, 1, 0, "c") 
    expected = ["cccc"]
    assert result == expected    

def test_GivenReplacementChar_WhenMapper_ThenFilledWithChar():
    grid = ["#....#"]
    result = floodfill.mapper(grid, 1, 0, "c") 
    expected = ["#cccc#"]
    assert result == expected

def test_GivenSplitAreas_WhenMapper_ThenOnlyFillContiguousArea():
    grid = ["#....#....#"]
    result = floodfill.mapper(grid, 1, 0, "c") 
    expected = ["#cccc#....#"]
    assert result == expected

def test_GivenCoordsOnRight_WhenMapper_ThenOnlyFillContiguousArea():
    grid = ["#....#....#"]
    result = floodfill.mapper(grid, 4, 0, "c") 
    expected = ["#cccc#....#"]
    assert result == expected

def test_GivenCoordsNotOnEdge_WhenMapper_ThenOnlyFillContiguousArea():
    grid = ["#........#....#"]
    result = floodfill.mapper(grid, 4, 0, "c") 
    expected = ["#cccccccc#....#"]
    assert result == expected

def test_GivenStartPointBetweenBorders_WhenMapper_ThenFillOnlyContiguous():
    grid = ["#....#....#....#"]
    result = floodfill.mapper(grid, 6, 0, "c")
    expected = ["#....#cccc#....#"]
    assert result == expected

def test_GivenGridOnMultipleLines_WhenMapper_ThenFillContiguous():
    grid = [
        "#....#",
        "#....#"
    ]
    result = floodfill.mapper(grid, 1, 0, "c")
    expected = [
        "#cccc#",
        "#cccc#"
    ]
    assert result == expected

def test_GivenSampleImage1_WhenMapper_ThenFillCorrectAreas():
    with open("tests/images/sample_image1.txt", "r") as f:
        grid = [line.rstrip() for line in f]
    result = floodfill.mapper(grid, 8, 12, "@")
    with open("tests/images/sample_image1_result.txt", "r") as r:
        expected = [line.rstrip() for line in r]
    assert result == expected

def test_GivenSampleImage2_WhenMapper_ThenFillCorrectAreas():
    with open("tests/images/sample_image2.txt", "r") as f:
        grid = [line.rstrip() for line in f]
    result = floodfill.mapper(grid, 2, 2, "@")
    with open("tests/images/sample_image2_result.txt", "r") as r:
        expected = [line.rstrip() for line in r]
    assert result == expected

def test_GivenSampleImage3_WhenMapper_ThenFillCorrectAreas():
    with open("tests/images/sample_image3.txt", "r") as f:
        grid = [line.rstrip() for line in f]
    result = floodfill.mapper(grid, 8, 3, ",")
    with open("tests/images/sample_image3_result.txt", "r") as r:
        expected = [line.rstrip() for line in r]
    assert result == expected
