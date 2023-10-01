def pig_latin(sentence):
    """
    A simple english to pig latin translation fxn for full sentences.
    Takes a single english word or sentence as input, and returns translated pig latin.

    """
    translation = ''
    for word in sentence.split():
        if word[0] in 'aeiou':
            translated_word = word + "way "
            translation += translated_word
        else:
            translated_word = word[1:] + word[0] + "ay "
            translation += translated_word

    return translation


translation = pig_latin('what is pig latin')
print(translation)
