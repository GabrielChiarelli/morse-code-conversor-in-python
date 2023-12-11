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
<p>When converting a morse code into english, you can convert just one word, or two or more.</p>
<p>When converting two or more, be sure to use the <em>sep</em> parameter to indicate where the whitespace of the sentence is.</p>
<p>I.e. if you want to write ".... . .-.. .-.. ---&nbsp&nbsp.... .. (that is "hello hi"), be sure to write ".... . .-.. .-.. --- ~ .... .." (where the "~" is the <em>sep</em> parameter, indicating that the sentence has a whitespace there.</p>
<p>(you can change the <em>sep</em> parameter to wherever char you wish, as long as it's not a char used in the dict of chars that we use to convert.) 😀</p>
