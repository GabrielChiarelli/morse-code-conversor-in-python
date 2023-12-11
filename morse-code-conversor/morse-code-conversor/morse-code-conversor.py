# Morse Code Conversor
# Developed by Gabriel Chiarelli
# V1.0 - 11/12/2023

MORSE_CODE: dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..",


    " ": " ", ".": ".-.-.-", ",": "--..--", ":": "---...", ";": "-.-.-.",
    "'": ".----.", '"': ".-..-.", "-": "-....-", "_": "..--.-", "/": "-..-.",
    "?": "..--..", "!": "-.-.--", "&": ".-...", "$": "...-..-", "@": ".--.-.",
    "(": "-.--.", ")": "-.--.-", "+": ".-.-.", "=": "-...-",


    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

ENGLISH_CODE: dict = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
    "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
    "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
    "--..": "z",


    " ": " ", ".-.-.-": ".", "--..--": ",", "---...": ":", "-.-.-.": ";",
    ".----.": "'", ".-..-.": '"', "-....-": "-", "..--.-": "_", "-..-.": "/",
    "..--..": "?", "-.-.--": "!", ".-...": "&", "...-..-": "$", ".--.-.": "@",
    "-.--.": "(", "-.--.-": ")", ".-.-.": "+", "-...-": "=",


    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
}

def convert_to_morse(str_to_convert: str) -> str:
    """
    Returns the str passed by the user (in english) in morse code format.

    :param str str_to_convert: The str to be converted to morse code
    :return: the str in morse code
    :rtype: str:
    :raises TypeError: if the str_to_convert is not a str
    """

    if type(str_to_convert) != str:
        raise TypeError("The 'convert_to_morse()' function needs a str as an argument.")


    str_in_morse: str = ""
    
    for index, char in enumerate(str_to_convert.lower()):
        if char in MORSE_CODE:
            if index < len(str_to_convert)-1:
                str_in_morse += MORSE_CODE[char] + " "
            else:
                str_in_morse += MORSE_CODE[char]
        else:
            raise ValueError(f"The char in position {index} ('{char}') does not exist in morse code.")

    return str_in_morse


def convert_to_english(str_to_convert: str, sep: str="~") -> str:
    """
    Return the str passed by the user (in morse code) in english.

    :param str str_to_convert: The str to convert to english
    :param str sep: The char used to indicate that a 'space' in the str is, indeed, a 'space'; can be any char that are not in the ENGLISH_CODE dict
    :return: the str_to_convert in english
    :rtype: str
    :raises TypeError: if the str_to_convert is not a str
    :raises TypeError: if the stp is not a str
    """

    if type(str_to_convert) != str:
        raise TypeError("The 'convert_to_morse()' function needs a str as an argument for 'str_to_convert'.")
    elif type(sep) != str:
        raise TypeError("The 'convert_to_morse()' function needs a str as an argument for 'sep'")
    

    str_to_convert = str_to_convert.lower().split(" ")
    str_in_english: str = ""

    if sep in str_to_convert:
        for index, word in enumerate(str_to_convert):
                if word in ENGLISH_CODE:
                    str_in_english += ENGLISH_CODE[word]
                elif word == sep:
                    str_in_english += " "
                else:
                    raise ValueError(f"The char in position {index} ('{word}') does not exist in our language.")
    else:
        for index, char in enumerate(str_to_convert):
            if char in ENGLISH_CODE:
                str_in_english += ENGLISH_CODE[char]
            else:
                raise ValueError(f"The char in position {index} ('{char}') does not exist in our language.")
    
    return str_in_english
