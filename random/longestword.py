def longestWord(sentence):
    wordArray = sentence.split(" ")
    longest = ""
    for word in wordArray:
        if(len(word) >= len(longest)):
            longest = word
    return longest

print(longestWord("Hello World"))