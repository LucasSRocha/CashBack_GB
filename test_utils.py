import pytest

from .utils import clean_string_punctuation


@pytest.mark.parametrize(
    "input_string, output",
    [
        ("1234", "1234"),
        ("1.2.;3!4", "1234"),
        ("123.456.789-09", "12345678909"),
        ("this shouldn't have punctuation", "this shouldnt have punctuation"),
        ("a.b!c@D$%fG", "abcDfG"),
    ],
)
def test_clean_string_punctuation(input_string, output):
    assert clean_string_punctuation(input_string) == output
