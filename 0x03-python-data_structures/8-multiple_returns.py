#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or len(sentence) == 0:
        return len(sentence), None
    else:
        char = sentence[0]
        check = len(sentence), char
        return (check)
