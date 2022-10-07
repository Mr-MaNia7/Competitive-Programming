class Solution():
    def isValid(self, s: str) -> bool:
        bracketDict = {
            '(' : ')', '{' : '}', '[' : ']'
        }
        queue = list()
        for bracket in s:
            if bracket in bracketDict.values() and not queue:
                return False
            elif bracket in bracketDict.keys():
                queue.append(bracketDict[bracket])
            elif bracket == queue[-1]:
                queue.pop()
            else:
                return False
        if queue:
            return False
        return True
                    
if __name__ == "__main__":
    soln = Solution()
    print(soln.isValid("{[}]"))