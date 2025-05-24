class Solution(object):
    def isNumber(self, s):
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            int_part, dot, frac_part = s.partition('.')
            if not int_part and not frac_part:
                return False
            if int_part and not int_part.isdigit():
                return False
            if frac_part and not frac_part.isdigit():
                return False
            return True

        s = s.strip()
        if 'e' in s or 'E' in s:
            base, exp = s.lower().split('e', 1)
            return (isDecimal(base) or isInteger(base)) and isInteger(exp)
        return isDecimal(s) or isInteger(s)
