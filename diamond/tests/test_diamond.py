
import pytest
from diamond.app.diamondmaker import *

diamondmaker = DiamondMaker()

def test_GivenAAsInput_WhenChoosingLetter_ThenReturnA():
    assert diamondmaker.diamond("A") == "A", "A as input should return only A"

def test_GivenaAsInput_WhenChoosingLetter_ThenReturnA():
    assert diamondmaker.diamond("a") == "A", "Lowercase letters should be converted to uppercase"

def test_GivenBAsInput_WhenChoosingLetter_ThenReturnBDiamond():
    assert diamondmaker.diamond("B") == [" A ","B B"," A "], "Need to make a B diamond."

def test_GivenCOrHigher_WhenChoosingLetter_ThenCreateDiamond():
    assert diamondmaker.diamond("C") == ["  A  "," B B ","C   C"," B B ","  A  "]
    assert len(diamondmaker.diamond("F")[0]) == 11
    assert len(diamondmaker.diamond("F")) == 11

def test_GivenAAAsInput_WhenChoosingLetter_ThenReturnValueError():
    with pytest.raises(ValueError):
        diamondmaker.diamond("AA"), "Only single character inputs should be allowed"

def test_Given1AsInput_WhenChoosingLetter_ThenValueError():
    with pytest.raises(ValueError):
        diamondmaker.diamond("1"), "Only letters should be allowed"

def test_GivenNoneAsInput_WhenChoosingLetter_ThenTypeError():
    with pytest.raises(TypeError):
        diamondmaker.diamond(None), "Null is not allowed"
