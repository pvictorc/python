from exercises.pytest.romano_pra_decimal import RomanConverter


class TestRomanConverter:
    def test_to_decimal_simple(self):
        assert RomanConverter.to_decimal("IX") == 9
