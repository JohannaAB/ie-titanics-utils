import pytest
import pandas as pd
from numpy.testing import assert_almost_equal

from ie_utils import tokenize

@pytest.mark.parametrize("sentence, expected_tokens",[
    ("This is a sentence", ["This", "is", "a", "sentence"]),
    ("Another sentence", ["Another", "sentence"])
])

def test_tokenize_returns_expected_tokens(sentence, expected_tokens):
    tokens= tokenize(sentence)
    
    assert tokens == expected_tokens


def test_tokenize_lower_returns_lowercase_tokens():
    sentence = "Hello World!"
    expected_tokes = ("hello", "world!")
    tokens = tokenize(sentence, lower= True)

def test_series_are_equal():
    ser = pd.Series([0.1, 0.2, 0.1 + 0.2])
    expected_ser = pd.Series([0.1, 0.2, 0.3])
    assert_almost_equal(ser, expected_ser)
    
