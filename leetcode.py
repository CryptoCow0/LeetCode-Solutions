class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        Less_than_twenty = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ",
                             "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ",
                             "Eighteen ", "Nineteen "]

        Greater_than_twenty = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

        def underThousand(n):
            if n == 0:
                return ""
            if n < 20:
                return Less_than_twenty[n]
            if n < 100:
                return Greater_than_twenty[n // 10] + Less_than_twenty[n % 10]
            if n < 1000:
                return Less_than_twenty[n // 100] + "Hundred " + (underThousand(n % 100) if n % 100 != 0 else "")

        def numberoverThousand(n):
            if n < 1000:
                return underThousand(n)
            if n < 1_000_000:
                return underThousand(n // 1000) + "Thousand " + (underThousand(n % 1000) if n % 1000 != 0 else "")
            if n < 1_000_000_000:
                return underThousand(n // 1_000_000) + "Million " + (numberoverThousand(n % 1_000_000) if n % 1_000_000 != 0 else "")
            else:
                return underThousand(n // 1_000_000_000) + "Billion " + (numberoverThousand(n % 1_000_000_000) if n % 1_000_000_000 != 0 else "")

        if num == 0:
            return "Zero"
        return numberoverThousand(num).strip()
