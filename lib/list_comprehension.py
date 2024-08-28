#!/usr/bin/env python3

def return_evens(num_list):
    pass
    evens = [n for n in num_list if n % 2 == 0]
    return evens
# return_evens([1,2,3,4,5])


def make_exclamation(sentence_list):
    pass
    if sentence_list == []:
        return []
    exclaimed = [f'{n}!' for n in sentence_list]
    return (exclaimed)


# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
