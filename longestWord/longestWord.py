#!/usr/bin/python3
import re
def solution(text):
    text= re.split("[^a-zA-Z]+", text)
    maximum = 0
    max_word = ""
    word = ""
    for i in text:
        word = re.findall("[a-zA-Z]", i)
        answer = "".join(word)
        if maximum < len(answer):
            max_word = answer
            maximum = len(answer)
    return max_word
    