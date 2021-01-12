from PyDictionary import PyDictionary
import random

def generate_word():
    letter = "abcdefghijklmnopqrstuvwxyz"
    wlen = random.randint(4, 9)
    word = ""
    for x in range(wlen):
        wselect = random.randint(0, len(letter) - 1)
        word += letter[wselect]
    
    return word

dictionary=PyDictionary()
correctWord = None
numberWords = 3
listWords = []

for x in range(3):
    while not correctWord:
        testWord = generate_word()
        if dictionary.meaning(testWord):
            correctWord = testWord
    listWords.append(correctWord)
    correctWord = None
    

print("generated words: ", listWords)
#print("meaning: ", dictionary.meaning(correctWord))