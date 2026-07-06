frequency = {}

with open("demo.txt") as f:
    for x in f:
        words = x.split()
    

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1 



def findTopWordCount(dict):
    count = 0 
    topWord = ""

    for key, value in dict.items():
        if value > count:
            count = value
            topWord = key
    return topWord, count



# def findHigh(dictionary):
   
#     top = {}
#     count = 0 
#     newDic = {}
#     highestValue = 0 
#     highest = {}





#     if count > 1:
#         return top
#     else:
#         for key, value in dictionary.items():
#             if value < highestValue:
#                 newDic[key] = value
#             else:
#                 highestValue = value 
#                 highest.clear()
#                 highest[key] = value
                
#         findHigh(newDic)
#             count += 1

for i in range(5):
    word, cnt = findTopWordCount(frequency)
    print(word)
    print(cnt)
    frequency.pop(word)

# word2, cnt2 = findTopWordCount(frequency)
# print(word2)
# print(cnt2)
