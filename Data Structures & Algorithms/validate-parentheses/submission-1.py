class Solution:
    def isValid(self, s: str) -> bool:
        brack_stack = []
        bracket_matches = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for b in s:
            # Open bracket
            if b not in bracket_matches:
                brack_stack.append(b)
            else:
                if not brack_stack or brack_stack[-1] != bracket_matches[b]:
                    return False
                else:
                    brack_stack.pop()
        
        return not brack_stack
                
