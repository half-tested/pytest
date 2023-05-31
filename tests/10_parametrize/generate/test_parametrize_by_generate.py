def test_valid_string(stringinput):
    assert stringinput.isalpha()

# pytest tests/pytest/parametrize/generate/test_parametrize_by_generate.py --stringinput="hello" --stringinput="world" --stringinput="4317" -v

# A string is alpha-numeric if all characters in the string are alpha-numeric
# and there is at least one character in the string.
