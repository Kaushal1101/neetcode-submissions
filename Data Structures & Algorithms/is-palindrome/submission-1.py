class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        def same_alphabet(a, b):
            print(a.isalpha() and b.isalpha())
            return a.isalpha() and b.isalpha() and a.lower() == b.lower()
        
        def same_number(a, b):
            return a.isdigit() and b.isdigit() and a == b
        
        

        while lp < rp:
            if s[lp].isalnum() and s[rp].isalnum() and not (same_alphabet(s[lp], s[rp]) or same_number(s[lp], s[rp])):
                print(s[lp], s[rp])
                return False
            else:
                if not s[lp].isalnum():
                    lp += 1
                elif not s[rp].isalnum():
                    rp -= 1
                else:
                    lp += 1
                    rp -= 1
        
        return True