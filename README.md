A python script to convert your words into morse code and vice versa.

<h2>Usage</h2>
<hr>
<h3>Converting English into Morse Code:</h3>

```
import morse_code_conversor as mcc

def main():
    word_to_convert = input("Convert to morse code: ")
    print(mcc.convert_to_morse(str_to_convert=word_to_convert))


if __name__ == "__main__":
    main()

```

<h3>Converting Morse Code into English: </h3>

```
import morse_code_conversor as mcc

def main():
    morse_code_to_convert = input("Convert back to english: ")
    print(mcc.convert_to_english(str_to_convert=morse_code_to_convert, sep="~"))


if __name__ == "__main__":
    main()

```
