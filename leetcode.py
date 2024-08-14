Less_than_twenty = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]

greater = ["", "Ten ", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

string = ""

def underThousand(n):
    n = int(n)
    if n == 0:
        return ""

    if n < 20:
        return Less_than_twenty[n]
    
    if n < 100:
        return greater[n//10] + Less_than_twenty[n % 10]
    
    if n>= 100 and n < 1000:
        #print(Less_than_twenty[n // 100] + " Hundred " + greater[(n//10 )% 10] + Less_than_twenty[n% 10])
        return Less_than_twenty[n // 100] + "Hundred " + (underThousand(n % 100) if n % 100 != 0 else "")
    
    else:
        numberoverThousand(n)

def numberoverThousand(n):
    n = int(n)
    if n == 0:
        return "zero"

    #print(n)
    if n < 1_000:
        return underThousand(n)

    if n >= 1000 and n <= 19999:
        #print("I FOUND THE BUG")
        #print(n//1000)
        return Less_than_twenty[n // 1000] + "Thousand " + underThousand(n % 1000)
    
    if n >= 20_000 and n <= 99_999:
        return greater[n//10000] + Less_than_twenty[(n//1000) % 10] + "Thousand " + underThousand(n % 1000)

    if n >= 100_000 and n <=999_999:
        return Less_than_twenty[n//100_000] + "Hundred " + greater[n//10_000 % 10] + Less_than_twenty[n//1_000 % 10] + "Thousand" + (underThousand(n % 1000) if n %1000 != 0 else"")
    if n >= 1_000_000 and n <= 999_999_999:
        x = n - ((n // 1_000_000) * 1_000_000)
        number = underThousand(n/1_000_000)
        #print(number)
        #print(x)
        return number + "million " + numberoverThousand(x)
    else:
        y = n - ((n // 1_000_000_000) * 1_000_000_000)
        number = underThousand(n/1_000_000_000)
        return number + "Billion" + numberoverThousand(y)
    
       

x = input()

Answer = underThousand(x)

#print(Answer)
print(numberoverThousand(x))
    # 1000 and up

  