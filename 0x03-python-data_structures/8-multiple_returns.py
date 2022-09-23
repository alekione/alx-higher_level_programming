#!/usr/bin/python3

# retuns a turple of len of sentence and first character

def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, None
    return len(sentence), sentence[0]
