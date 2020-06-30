from re import findall


def clean_string_punctuation(string: str):
    return "".join(findall(r"\s?\w*\s?", string))
