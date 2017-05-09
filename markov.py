# markov.py - simple markov chain

import random

def build_chain(text, chain={}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    return chain


def generate_message(chain, count=140):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    if len(message) > 140:
        print 'tweet exceeds 140 characters - dropping last word'
        words = message.split(' ')
        message = words[0]
        del words[-1]
        for word in words[1:]:
            message += ' ' + word
        print 'tweet is now %s characters long' % len(message)
        print '-'*10
    return message


def read_file(filename):
    with open(filename, "r") as file:
        contents = file.read().replace('\n\n', ' ')
    return contents


def write_file(filename, message):
    with open(filename, "w") as file:
        file.write(message)