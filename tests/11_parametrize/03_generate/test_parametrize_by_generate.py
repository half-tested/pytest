def test_parametrize_by_generate(stringinput):
    assert stringinput.isalpha()


def test_not_parametrize_by_generate():
    pass

# pytest tests/11_parametrize/03_generate --stringinput="hello" --stringinput="world" --stringinput="4317"

# A string is alpha-numeric if all characters in the string are alpha-numeric
# and there is at least one character in the string.
