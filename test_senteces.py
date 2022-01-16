from os import path
from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(3):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
def test_get_noun():
    #Test the single nouns.
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        noun = get_noun(1)

        assert noun in single_nouns
    #Test the plural nouns.
    plural_nouns = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(10):
        noun = get_noun(2)

        assert noun in plural_nouns
def test_get_verb():
    #Test the past verbs
    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(10):
        past_verb = get_verb( '','past')

        assert past_verb in past
    #Test the present verb in third person
    present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(10):
        present_verb = get_verb(1,'present')

        assert present_verb in present
    #Test the present verb in plural
    presents = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(10):
        presents_verb = get_verb(2,'present')

        assert presents_verb in presents
    #Test the future verb
    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(10):
            future_verbs = get_verb('','')
            assert future_verbs in future
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(30):
        preposition =  get_preposition(1)
        assert preposition in prepositions
def test_get_prepositional_phrase():
    #TEST SINGLE PREPOSITIONAL PHRASE
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    #This help me to know that the phrase that i get when i use the get_prepositional_phrase contains one of the preposition in the list.
    for _ in range(30):
        preposition =  get_prepositional_phrase(1)
        divide = preposition.split()
        preposition = divide[0]
        assert preposition in prepositions

    #This help me to know that the phrase that i get when i use the get_prepositional_phrase contains one of the single determiners in the list.

    single_determiners = ["a", "one", "the"]


    for _ in range(3):
        determiner = get_prepositional_phrase(1)
        divide = determiner.split()
        determiner = divide[1]
        
        assert determiner in single_determiners
    #This help me to know that the phrase that i get when i use the get_prepositional_phrase contains one of the single determiners in the list.

    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        noun = get_prepositional_phrase(1)
        divide = noun.split()
        noun = divide[2]
        assert noun in single_nouns


    #    #TEST PLURAL PREPOSITIONAL PHRASE

    #test plural nouns
    plural_nouns = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(10):
        noun = get_prepositional_phrase(2)
        divide = noun.split()
        noun = divide[2]

        assert noun in plural_nouns
    #test plural determiner
    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):
        determiner_plural = get_prepositional_phrase(2)
        divide = determiner_plural.split()
        determiner_plural = divide[1]
        assert determiner_plural in plural_determiners

    # assert phrase == (lol).split(',')
pytest.main(["-v", "--tb=line", "-rN", __file__])