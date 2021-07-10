from random import randint
import copy
story = (
        " Today I went to the zoo. I saw a/an {} {} jumping up and down in its tree." +
        " He {} {} through the large tunnel that led to its {} {}. " +
        " I got some peanuts and passed them through the cage to a gigantic gray {} towering above my head." +
        " Feeding that animal made me hungry." +
        " I went to get a {} scoop of ice cream." +
        " It filled my stomach." +
        " Afterwards I had to {} {} to catch our bus." +
        " When I got home I {} my mom for a {} day at the zoo."
)
word_dict = {
    'adjective' : ['scandalous', 'curly', 'willing', 'superb', 'outstanding'],
    'noun' : ['audience', 'king', 'instruction', 'pollution', 'knowledge', 'moment'],
    'verb' : ['wrote', 'ran', 'planted', 'cut', 'felt', 'planted'],
    'adverb' : ['neatly', 'hopelessly', 'copiously', 'badly']
}

def get_word(type, local_dict):
    word = local_dict(type)
    count = len(word) - 1
    index = randint(0, count)
    return local_dict[type].pop(index)

def create_fxn():
    local_dict = copy._deepcopy_dict(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('verb', local_dict),
        get_word('adverb', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('verb', local_dict),
        get_word('adverb', local_dict),
        get_word('verb', local_dict),
        get_word('adjective', local_dict),

    )
print("STORY 1: ")
print(create_fxn())
print()