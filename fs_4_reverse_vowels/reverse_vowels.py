def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    VOWELS = 'aeiouAEIOU'
    s_vowels = ''

    # takes vowels, replaces them with "="
    for char in s:
        if char in VOWELS:
            s_vowels += char
            s = s.replace(char, "=")

    # reverses vowels string
    s_vowels = s_vowels[::-1]

    # replaces "=" one by onewith reversed vowels
    for i in range(len(s_vowels)):
        s = s.replace("=", s_vowels[i], 1)

    return s