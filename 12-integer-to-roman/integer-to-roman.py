class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        roman_numeral = []
        for value, symbol in val_to_roman:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_numeral.append(symbol * count)
        
        return ''.join(roman_numeral)
