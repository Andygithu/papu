import random
def main():
    
    #Generate  a sentence in past-singular.
    determiner_singular = get_determiner(1)
    noun_singular = get_noun(1)
    verb_past = get_verb('','past')
    preposition_phrase_1 = get_prepositional_phrase(1)
    preposition_phrase = get_prepositional_phrase(1)
    print(f'{determiner_singular.capitalize()} {noun_singular} {verb_past} {preposition_phrase_1} {preposition_phrase}.')
    #Generate a sentence in present-singular
    determiner_singular = get_determiner(1)
    noun_plural = get_noun(1)
    verb_present = get_verb(1,'present')
    preposition_phrase_1 = get_prepositional_phrase(1)
    preposition_phrase = get_prepositional_phrase(1)
    print(f'{determiner_singular.capitalize()} {noun_plural} {verb_present} {preposition_phrase_1} {preposition_phrase}.')
    #Generate sentences in singular-future
    determiner_singular = get_determiner(1)
    noun_singular = get_noun(1)
    verb_future = get_verb('','')
    preposition_phrase_1 = get_prepositional_phrase(1)
    preposition_phrase = get_prepositional_phrase(1)
    print(f'{determiner_singular.capitalize()} {noun_singular} {verb_future} {preposition_phrase_1} {preposition_phrase}.')
    #Generate sentences in plural-past
    determiner_plural = get_determiner(2)
    noun_plural = get_noun(2)
    verb_past = get_verb('','past')
    preposition_phrase_1 = get_prepositional_phrase(2)
    preposition_phrase = get_prepositional_phrase(2)
    print(f'{determiner_plural.capitalize()} {noun_plural} {verb_past} {preposition_phrase_1} {preposition_phrase}.')
    #Generate sentences in plural-present
    determiner_plural = get_determiner(2)
    noun_plural = get_noun(2)
    verb_present = get_verb(2,'present')
    preposition_phrase_1 = get_prepositional_phrase(2)
    preposition_phrase = get_prepositional_phrase(2)
    print(f'{determiner_plural.capitalize()} {noun_plural} {verb_present} {preposition_phrase_1} {preposition_phrase}.')
    #Generate sentences in plural-future
    determiner_plural = get_determiner(2)
    noun_plural = get_noun(2)
    verb_future = get_verb('','')
    preposition_phrase_1 = get_prepositional_phrase(2)
    preposition_phrase = get_prepositional_phrase(2)
    print(f'{determiner_singular.capitalize()} {noun_plural} {verb_future} {preposition_phrase_1} {preposition_phrase}. ')
    
    
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_noun(quantity):
    
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    #Choose randomly a noun
    nouns = random.choice(nouns)
    return nouns


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past' and quantity == '':
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    #Choose randomly a noun
    verbs = random.choice(verbs)
    return verbs
def get_preposition(quantity):
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    if quantity == 1:


      prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition
def get_prepositional_phrase(quantity):
    if quantity == 1:
        #singular phrase
        preposition = get_preposition(1)
        determiner = get_determiner(1)
        noun = get_noun(1)
        phrase = (f'{preposition} {determiner} {noun}')
        return phrase
        
    else:
        preposition = get_preposition(1)
        determiner = get_determiner(2)
        noun = get_noun(2)
        phrase = (f'{preposition} {determiner} {noun}')
        return phrase


        

        

main()