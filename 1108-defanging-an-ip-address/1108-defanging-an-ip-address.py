class Solution:
    def defangIPaddr(self, address: str) -> str:
        f = ""
        for i, c in enumerate(address):
            if c == ".":
                f += "[.]"
            else:
                f += c
        return f