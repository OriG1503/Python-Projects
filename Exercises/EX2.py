"""
משימה :
לקלוט רצף מספרים עד שנקלט המספר 0
להדפיס את אורך הרצף העולה הגדול ביותר

דוגמה:
2 2 4 2 2 0 -> 2 4 -> 2

דוגמה:
1 5 14 2 8 11 12 4 1 6 0 -> 2 8 11 12 -> 4
"""

def collecting_nums():
    numList = []
    num = 0

    num = int(input("Enter a number: "))
    while(num!=0):
        numList.append(num)
        num = int(input("Enter a number: "))
    
    return numList

def rising_series_len_lst(numList, length):
    len = 1
    lenList = []
    for i in range(1 , length):
        num1 = numList[i-1]
        num2 = numList[i]
        if(num2>num1):
            len+=1
        elif(num2<num1):
            lenList.append(len)
            len = 1

    return lenList

def max_in_lst(lenList):
    return max(lenList)

def main():
    numList = collecting_nums()
    lenList = rising_series_len_lst(numList,len(numList))
    print(max_in_lst(lenList))

main()