import random

"""
Assignment 4
Due: April 17, 2020 at 16:30

student: SANTIAGO YEPES
student #: 301082274

"""

'''
Submit a zip file into the Assignment4 dropbox containing your python code and the accompanying text files.
All files and code must be able to run on Linux.

The scenario:
Sentences in any language have a structure defined by a set of grammar rules.
They also include a set of words from the vocabulary of the language.
The vocabulary of a language like English consists of many thousands of words, and the grammar rules are quite complex.
For the sake of simplicity, your program will generate sentences from a simplified subset of English.
The vocabulary will consist of sample words from several parts of speech, including nouns, verbs, articles, and prepositions.
From these words, you can build noun phrases, prepositional phrases, and verb phrases. From these constituent phrases, you can build sentences.
For example, the sentence, "The girl hit the ball with the bat," contains three noun phrases, one verb phrase, and one prepositional phrase.

The rule for Noun phrase says that it is an Article followed by (+) a Noun. Thus, a possible noun phrase is "the bat."
Note that some of the phrases are constituents of other phrases.
Although this grammar is much simpler than the complete set of rules for English grammar,
you should still be able to generate sentences with quite a bit of structure.
The program will prompt the user for the number of sentences to generate.

6 marks
Question 1)
Modify the sentence-generator program below so that it inputs its vocabulary from a set of text files at startup.
The file names are nouns.txt, verbs.txt, articles.txt, and prepositions.txt.
(Hint: Define a single new function, getWords. This function should expect a filename as an argument.
The function should open an input file
with this name, define a temporary list, read words from the file, and add them to the list.
The function should then convert the list to a tuple and return this tuple.
Call the function with an actual filename to initialize each of the four variables for the vocabulary.
'''

"""
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""


# defining function to read a file, and store data into a list or tuple
def get_words(input_file):
    temp_file = open(input_file, 'r')
    words_tuple = tuple(temp_file.read().strip().splitlines())
    return words_tuple


# store files into variables
articles = get_words('articles.txt')
nouns = get_words('nouns.txt')
verbs = get_words('verbs.txt')
prepositions = get_words('prepositions.txt')
adjectives = get_words('adjectives.txt')
conjunctions = get_words('conjunctions.txt')

'''
9 marks
Question 2)
Make the following modifications to the original sentence-generator
program:
a) The prepositional phrase is optional. (It can appear with a certain
probability.)
b) A conjunction and a second independent clause are optional: The
boy took a drink and the girl played baseball.
c) An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions
'''


# defining a function to return or not an argument (the argument will call any phrase method)
def optional_phrase(phrase_method):
    if random.randint(0, 2) > 0:
        return phrase_method
    else:
        return ""


def sentence():
    # Builds and returns a sentence.
    return noun_phrase() + " " + verb_phrase() + " " + \
           optional_phrase(random.choice(conjunctions) + " " + noun_phrase() + " " + verb_phrase())


def noun_phrase():
    # Builds and returns a noun phrase.
    return random.choice(articles) + " " + optional_phrase(random.choice(adjectives)) + " " + random.choice(nouns)


def verb_phrase():
    # Builds and returns a verb phrase.
    return random.choice(verbs) + " " + noun_phrase() + " " + optional_phrase(prepositional_phrase())


def prepositional_phrase():
    # Builds and returns a prepositional phrase.
    return random.choice(prepositions) + " " + noun_phrase()


def main():
    # Allows the user to input the number of sentences to generate.
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


main()
