class Solution1:
    def romanToInt(self, s: str) -> int:
        i = 0
        int_value = 0
        while i < len(s):
            match s[i]:
                case 'I':
                    if i+1 < len(s) and s[i+1] == 'V':
                        int_value += 4
                        i += 1
                    elif i+1 < len(s) and s[i+1] == 'X':
                        int_value += 9
                        i += 1
                    else:
                        int_value += 1
                case 'V':
                    int_value += 5
                case 'X':
                    if i+1 < len(s) and s[i+1] == 'L':
                        int_value += 40
                        i += 1
                    elif i+1 < len(s) and s[i+1] == 'C':
                        int_value += 90
                        i += 1
                    else:
                        int_value += 10
                case 'L':
                    int_value += 50
                case 'C':
                    if i+1 < len(s) and s[i+1] == 'D':
                        int_value += 400
                        i += 1
                    elif i+1 < len(s) and s[i+1] == 'M':
                        int_value += 900
                        i += 1
                    else:
                        int_value += 100
                case 'D':
                    int_value += 500
                case 'M':
                    int_value += 1000
            i += 1
        return int_value  


class Solution:
    def romanToInt(self, s: str) -> int:
        dico = { 'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 
            'XL': 40, 'L':50, 'XC':90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000 
        }
        i = 0
        int_value = 0
        for i in range(len(s)):
            if i+1 < len(s) and dico[s[i]] < dico[s[i+1]]:
                int_value -= dico[s[i]]
            else:
                int_value += dico[s[i]]
        return int_value 