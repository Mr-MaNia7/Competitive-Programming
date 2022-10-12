from typing import List

class Solution():
    def compress(self, chars):
        length = len(chars)
        if length < 2:
            return length
        anchor, write = 0, 0
        for pos, char in enumerate(chars):
            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1
                if pos > anchor:
                    repeated_times = pos - anchor + 1
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1
                anchor = pos + 1
        return write

if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))