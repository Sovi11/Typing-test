# typing test 
# First we will ask what to input. Initially we will just take this input and find a formula for word per minute.
import time
import random 
import pandas as pd
csv_words = pd.read_csv("unigram_freq.csv")
list_of_words = list((csv_words[0:1000])["word"])
avg_word_length = 5
def evaluation_accuracy1() : 
    # this evaluation just checks if string text to be entered matches with the user inputted string 
    return 100*(user_string==text_to_be_entered)
    # definitely a garbage approach to solve problem
def evaluation_accuracy2():
    # this is also a garbage approach but what people might expect 
    cnt = 0 
    for i in range(min(len(text_to_be_entered),len(user_string))):
        if text_to_be_entered[i]==user_string[i]: cnt+=1 
    return 100*(cnt/len(text_to_be_entered))
    # in practice the problem with this is... this does not penalize unnecessary garbage.
def evaluation_accuracy3():
    cnt = 0 
    for i in range(min(len(text_to_be_entered),len(user_string))):
        if text_to_be_entered[i]==user_string[i]: cnt+=1 
    cnt -= max((len(user_string)) - len(text_to_be_entered),0)
    return 100*(cnt/len(text_to_be_entered))
    # problem with this is that a character shift will be disastrous to this thing.
def evaluation_accuracy4_temp(word1,word2) : 
    # """Dynamic programming solution"""
    # this is the classic edit distance question
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table[-1][-1]
def evaluation_accuracy4():
    m= len(text_to_be_entered)
    n= len(user_string)
    incorr = evaluation_accuracy4_temp(text_to_be_entered,user_string)
    return 100*(1 - incorr/min(m,n))
def raw_wpm(endtime, starttime, num_words) : 
    t_diff_sec = (endtime- starttime) # hopefully in seconds
    return (num_words*60) / t_diff_sec

def wpm1(raw_wpm, accuracy) :
    return (raw_wpm*accuracy )/100

def num_words1() : 
    return len(user_string)/ avg_word_length
# list_of_words = ["hi", "hello","what","is"] 
# list of words should be replaced with words of english language 
# it should represent a good sample
text_to_be_entered = ""
# the code below is limited number of words to type format
print("How many words do you wish to type :")
x = int(input())
for i in range(x-1) : 
    ind1 = random.randint(0,len(list_of_words)-1)
    text_to_be_entered+= list_of_words[ind1]
    text_to_be_entered+=" "
ind1 = random.randint(0,len(list_of_words)-1)
text_to_be_entered+= list_of_words[ind1]
print(text_to_be_entered)
s = "\nEnter the text above without any enters :"
print(s)
# start the time here.
print("Press enter key to start timer")
input()
start_time= time.time()
user_string = input()
end_time = time.time()
if len(user_string) == 0 : print("Wrong input detected")
else:
# end the time here.
    num_words = num_words1()
    k= raw_wpm(end_time,start_time,num_words)
    acc = evaluation_accuracy4()
    # print(evaluation_accuracy1())
    # print(evaluation_accuracy2())
    # print(evaluation_accuracy3())
    print("Summary : ")
    print("Accuracy of the typing test is:")
    print(round(evaluation_accuracy4(),2))
    print("Raw WPM of the typing test is:")
    print(round(raw_wpm(end_time,start_time,num_words),2))
    print("Adjusted WPM of the typing test is:")
    print(round(wpm1(k,acc),2))
    # print(evaluation_accuracy4(input(),input()))
    # there should be a limited time format 

    # => complete that
    # things to do ::
    # 1. complete the evaluation function => done
    # 2. find a good list of words => done
    # 3. import time => done 
    # 4. Make other formats => limited time ? 
    # 5. In the limited word format to.. why not fetch sentences directly. ? 

