"""
משימה :
לקלוט מספרים עד שנקלט המספר 1-
להדפיס את המספר עם הכי הרבה ספרות שיש
במידה ויש כמה מספרים עם הכי הרבה ספרות (שזה גם הכמות הכללית הכי גדולה כמובן)
יודפס המספר הכי קטן מבניהם
"""

def digit_count(num):
    if (num == 0):
        return 0
    return digit_count(num//10)+1

def collecting_nums():
    numList = []
    num=0
    maxDigits = 0
    digits = 0

    num = int(input("Enter a number: "))

    while(num!=-1):
        numList.append(num)
        digits = digit_count(num)
        if(digits>maxDigits):
            maxDigits = digits

        num = int(input("Enter a number: "))
    
    return numList, maxDigits

def create_max_list(numList, maxDigits):
    maxList = []

    for num in numList:
        if(digit_count(num)==maxDigits):
            maxList.append(num)

    return maxList

def find_min_num_from_maxList(maxList):
    return min(maxList)

def main():
   numlist= []
   numList, maxDigits = collecting_nums()
   print("numList:",numList)
   maxList = create_max_list(numList, maxDigits)
   print("maxList:",maxList)
   minOfMaxDigit = find_min_num_from_maxList(maxList)
   print("The Final Number Is:",minOfMaxDigit)
  
main()
    