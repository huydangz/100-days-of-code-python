MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
SPLITTER_BW_LETTERS = ' '
SPLITTER_BW_WORDS = '   '


def is_last(_item, _list):
    return _list.index(_item) == len(_list) - 1


def encode(raw_text):
    result = ''
    words = raw_text.split(' ')
    for word in words:
        for letter in word:
            result += MORSE_CODE_DICT[letter.upper()]
            if not is_last(letter, word):
                result += SPLITTER_BW_LETTERS  # add SPLITTER gap between letters
            elif not is_last(word, words):
                result += SPLITTER_BW_WORDS  # add SPLITTER gap between letters
    return result


def decode(text_encoded):
    result = ''
    words_encoded = text_encoded.split(SPLITTER_BW_WORDS)
    for word_encoded in words_encoded:
        letters_encoded = word_encoded.split(SPLITTER_BW_LETTERS)
        for letter_encoded in letters_encoded:
            index = list(MORSE_CODE_DICT.values()).index(letter_encoded)  # get index of value in list
            result += list(MORSE_CODE_DICT.keys())[index]  # then get key in list by index
        if not is_last(word_encoded, words_encoded):
            result += ' '  # add space between words
    return result


text = input('Please type text input: ')
print(encode(text))
print(decode(encode(text)))

