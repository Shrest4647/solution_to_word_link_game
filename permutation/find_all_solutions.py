import sqlite3

inp = input("Enter all the characters")
db = sqlite3.connect("Dictionary.db")
word_of_2 = set()
word_of_3 = set()
word_of_4 = set()
word_of_5 = set()
word_of_6 = set()
def print_correct(word_of):
    for x in word_of:
        for w in db.execute("SELECT DISTINCT (word) FROM words WHERE word ='{}'".format(x)):
            print(w[0])
# def spellcheck(word,word_of_):
#     db = sqlite3.connect("Dictionary.db")
#
#     for wrd in db.execute("SELECT word FROM words WHERE word LIKE '*{}*'".format(inp[0])):
#         if wrd == word:
#             word_of_.append(word)
#             print(word)
#             break
#


for i in range(0,len(inp)):
     for j in range(0,len(inp)):
         if j != i:
             word2 = inp[i]+inp[j]
             #spellcheck(word2,word_of_2)
             #print(word2)
             #word_of_2.append(word2)
             word_of_2.add(word2)
             for k in range(0, len(inp)):
                 if k!= i and k!=j:
                    word3 = inp[i] + inp[j] + inp[k]
                    # spellcheck(word3,word_of_3)
                    word_of_3.add(word3)
                    #word_of_3.append(word3)
                    for l in range(0, len(inp)):
                        if l!= i and l!=j and l!=k:
                            word4 = word3 + inp[l]
                            # spellcheck(word4,word_of_4)
                            word_of_4.add(word4)
                            #word_of_4.append(word4)
                            for m in range(0,len(inp)):
                                if m!=i and m!=j and m!=k and m!=l:
                                    word5 = word4 + inp[m]
                                    # spellcheck(word5,word_of_5)
                                    word_of_5.add(word5)
                                    #word_of_5.append(word5)
                                    for n in range(0,len(inp)):
                                         if n!=i and n!=j and n!=k and n!=l and n!=m:
                                             w6 = word5 + inp[n]
                                             word_of_6.add(w6)

print("The two letters word are")
print_correct(word_of_2)
# for ans in word_of_2:
#     if spellcheck(ans):
#         print(ans,end=" ")
#
#
print("-" * 10 + "\n")
#
print("The three letters word are")
print_correct(word_of_3)
# for ans in word_of_3:
#     if spellcheck(ans):
#         print(ans,end=" ")
#
#
print("-" * 10 + "\n")
#
print("The four letters word are")
print_correct(word_of_4)
# for ans in word_of_4:
#     if spellcheck(ans):
#         print(ans,end=" ")
#
#
print("-" * 10 + "\n")
#
print("The five letters word are")
print_correct(word_of_5)
# for ans in word_of_5:
#     if spellcheck(ans):
#         print(ans, end=" ")
#
#
print("-" * 10 + "\n")

print("The six letters word are")
print_correct(word_of_6)
#
#
print("-" * 10 + "\n")
db.close()

input("Press any key to close")
