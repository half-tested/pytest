class TestMath:
    def test_class_multiplication(self):
        assert 3 * 4 == 12

    def test_class_addition(self):
        assert 2 + 2 != 4, "addition should work based on REQ-123"

    def test_class_division(self):
        assert 10 / 5 == 2

    # non-default naming conventions should be added to pytest.ini
    def check_class_subtraction(self):
        assert 5 - 3 == 2

    def test_class_modulus(self):
        assert 10 % 3 == 1

    def test_class_greater_than(self):
        assert 5 > 3

    def test_class_less_than(self):
        assert 2 < 4

    def test_class_equal_to(self):
        assert 6 == 6

    def test_class_not_equal_to(self):
        assert 3 != 4

class CheckInclude:
    def test_class_is_in(self):
        assert "a" in "abc"

    def test_class_is_not_in(self):
        assert "d" not in "abc"
