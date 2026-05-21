
class RomanConverter:
    """Simple converter from Roman numerals to decimal numbers."""

    _VALUES = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    @classmethod
    def to_decimal(cls, romano):
        """Convert a Roman numeral string to its decimal value."""
        if not romano or not isinstance(romano, str):
            return 0

        total = 0
        previous_value = 0

        for char in romano.upper():
            value = cls._VALUES.get(char, 0)
            if value == 0:
                return 0

            if value > previous_value:
                total += value - 2 * previous_value
            else:
                total += value

            previous_value = value

        return total


def romano_para_decimal(romano):
    """Legacy helper for the simple Roman numeral converter."""
    return RomanConverter.to_decimal(romano)
