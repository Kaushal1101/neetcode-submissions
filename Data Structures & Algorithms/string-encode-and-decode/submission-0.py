class Solution:

    def encode(self, strs: List[str]) -> str: 
        full_string = []
        for string in strs:
            for char in string:
                val = str(ord(char)) + "/"
                full_string.append(val)
            full_string.append("-")
        #print(full_string)
        return "".join(full_string)


    def decode(self, s: str) -> List[str]:
        strings = []
        curr_string = []
        curr_char = ""
        for char in s:
            if char == "/":
                curr_string.append(chr(int(curr_char)))
                curr_char = ""
            elif char == "-":
                strings.append("".join(curr_string))
                curr_string = []
            else:
                curr_char += char

        #print(strings)
        return strings