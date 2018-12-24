word = 'word'
sentence = "This is a sentence"
paragraph = """This is a paragraph.
It is multiline"""
raw = r"escape character \not interpreted"
multiple = 3 * "a"
autoConcat = "This is " "concatenated"
firstLetter = ("ABC")[0]
lastLetter = ("ABC")[-1]
sliceString = ("This is a slice of text")[10:15] #Negatives too, Empty too
length = len(sliceString)


print(word)
print(sentence)
print(paragraph)
print(raw)
print(multiple)
print(autoConcat)
print(firstLetter)
print(lastLetter)
print(sliceString)
