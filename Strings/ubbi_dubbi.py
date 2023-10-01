def ubbi_dubbi(word):
    """
    A simple function that translates an english word into secret ubbi dubbi language.
    """
    # check for vowels in word
    translation = ['ub' + char if char in 'aeiou' else char for char in word]
    return ''.join(translation)

    # # long way
    # translation = []
    # for char in word:
    #     if char in 'aeiou':
    #         translation.append(f"ub{char}")
    #     else:
    #         translation.append(char)
    # return ''.join(translation)


translation = ubbi_dubbi('python')
print(translation)
