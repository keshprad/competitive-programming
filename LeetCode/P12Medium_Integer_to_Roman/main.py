class Solution:
    def __init__(self):
        self.conversions = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

    def intToRoman(self, num: int) -> str:
        roman = ""
        for (symbol, value) in self.conversions.items():
            roman += num//value * symbol
            num %= value
        return roman
