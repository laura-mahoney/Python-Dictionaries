"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    empty_dictionary = {} #est a dictionary
    
    phrase_words = phrase.split(" ") # this gives a list of words
    unique_words = set(phrase_words) # this turns list of words into unique set 
    for word in unique_words:       #looping through the words in unique set
        empty_dictionary[word] = 0      #word added as key to dictionary

    for word in phrase_words:           #looping thtough the list
        if word in phrase_words:        #if word is in the list increment the dictionary value by 1
            empty_dictionary[word] += 1


    return empty_dictionary #returns dictionary with distinct words, and the number of times they appear


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # melon_prices = {
    #     "Watermelon": 2.95,
    #     "Cantaloupe": 2.50,
    #     "Musk": 3.25,
    #     "Christmas": 14.25}

       # for melon_type in melon_prices: 
    #     price = melon_prices[melon_name]
    #     return price

    # return "No price found"



    melon_prices = {                #created a dictionary with prices as values
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25}

    try:
        for melon_type in melon_prices:         #looped through the melon types to get their price
            price = melon_prices[melon_name]    #price is found using melon name key
            return price

    except:
        return "No price found"

 




def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    word_lengths = {}

    for word in words: 
        if len(word) in word_lengths:
            x = word_lengths[len(word)] 
            x.insert(0, word)
        else: 
            word_lengths[len(word)] = [word] 

    keys = sorted(word_lengths.keys())
    words_by_length = [(key, word_lengths[key]) for key in keys]

    return words_by_length

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    pirate_translator = {           #made a dictionary to map out words
        "sir": "matey", 
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart", 
        "restaurant": "galley", 
        "your": "yer", 
        "excuse": "arr", 
        "students": "swabbies", 
        "are": "be", 
        "restroom": "head", 
        "my": "me", 
        "is": "be"}


    phrase = phrase.split(" ")      #split the input and made a translation accumulator string
    translation = ""

    for word in phrase:             #looped through the words and if found, word translated to pirate speak, gets concatendated
        if word in pirate_translator: 
            translation = translation + " " + pirate_translator[word]
        else: 
            translation = translation + " " + word  #if word not found, it's left alone, and gets concatenated
    return translation.lstrip(" ")


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    result = {} #creating a result dictionary to store name, and last letter 
    
    name = names[0]       #first name is names at zero index
    last_letter = name[-1]
    result[name] = (names[0], last_letter)
     #last letter is at -1 index
                  #first key is start name, first value is last letter 
    
    
    for name in names[:len(names)-1:]: #looping through the list 
        if name not in result:
            
            if name[0] == last_letter:
                result[name] = (name, name[-1])
                last_letter = result[name][1]
            else:
    
                continue
                

    
    return result.keys()

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
