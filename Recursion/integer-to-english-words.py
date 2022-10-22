class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        powers = {2 : 'Hundred', 3 : 'Thousand', 6 : 'Million', 9 : 'Billion'}
        numStr = str(num)
        if num == 0:
            return 'Zero'
        elif num < 20:
            return ones[num]
        elif num < 100:
            return (tens[num // 10] + ' ' + ones[num % 10]).rstrip()
        elif num < 1000:
            if int(numStr[1:]) == 0:
                return ones[num // 100] + ' Hundred'
            return ones[num // 100] + ' Hundred ' + self.numberToWords(num % 100)
        elif num < 1000000:
            if int(numStr[-3:]) == 0:
                return self.numberToWords(int(numStr[:-3])) + ' Thousand'
            return self.numberToWords(int(numStr[:-3])) + ' Thousand ' + self.numberToWords(int(numStr[-3:]))
        elif num < 1000000000:
            if int(numStr[-6:]) == 0:
                return self.numberToWords(int(numStr[:-6])) + ' Million'
            return self.numberToWords(int(numStr[:-6])) + ' Million ' + self.numberToWords(int(numStr[-6:]))
        elif num < 1000000000000:
            if int(numStr[-9:]) == 0:
                return self.numberToWords(int(numStr[:-9])) + ' Billion'
            return self.numberToWords(int(numStr[:-9])) + ' Billion ' + self.numberToWords(int(numStr[-9:]))

if __name__ == "__main__":
    s = Solution()
    print(s.numberToWords(0))