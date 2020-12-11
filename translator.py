decode = {"-----":"0",
".----":"1",
"..---":"2",
"...--":"3",
"....-":"4",
".....":"5",
"-....":"6",
"--...":"7",
"---..":"8",
"----.":"9",
".-":"a",
"-...":"b",
"-.-.":"c",
"-..":"d",
".":"e",
"..-.":"f",
"--.":"g",
"....":"h",
"..":"i",
".---":"j",
"-.-":"k",
".-..":"l",
"--":"m",
"-.":"n",
"---":"o",
".--.":"p",
"--.-":"q",
".-.":"r",
"...":"s",
"-":"t",
"..-":"u",
"...-":"v",
".--":"w",
"-..-":"x",
"-.--":"y",
"--..":"z",
"/":" ",
"-.-.--":"!",
".-.-.-":".",
"--.--":","
}

encode = {"0":"-----",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
"a":".-",
"b":"-...",
"c":"-.-.",
"d":"-..",
"e":".",
"f":"..-.",
"g":"--.",
"h":"....",
"i":"..",
"j":".---",
"k":"-.-",
"l":".-..",
"m":"--",
"n":"-.",
"o":"---",
"p":".--.",
"q":"--.-",
"r":".-.",
"s":"...",
"t":"-",
"u":"..-",
"v":"...-",
"w":".--",
"x":"-..-",
"y":"-.--",
"z":"--..",
" ":"/",
"!":"-.-.--",
".":".-.-.-",
",":"--.--"
}

# Try a methos that uses two matching lists (instead of dictionaries), one for morse and one for plain text, that have the positions lined up

def decoding(morse_text):
    translated = ''
    morse_text = morse_text.split('/')
    for char in morse_text:
        print(char)
        morse_letter = decode[char]
        translated += morse_letter + " "
    return translated

def encoding(plain_text):
    translated = ''
    for char in plain_text:
        print(char)
        morse_letter = encode[char.lower()]
        if morse_letter == '/':
            pass
        else:
            translated += morse_letter + '/'
    translated = translated[:-1]
    return translated

print("Morse Code Translator\n")

choice = 0

while choice != 3:

    choice = int(input("""What would you like to do?

1. Decode a message
2. Encode a message
3. Exit program

1/2/3: """))

    if choice == 1:
        to_decode = input("Please enter your message to be decoded\n Note: Separate all characters with a  '/'\n> ")
        final = decoding(to_decode)
        print(f"Decoded message: {final}\n")
    elif choice == 2:
        to_encode = input("Please enter your message to be encoded\n Note: Separate all characters with a space\n> ")
        final = encoding(to_encode)
        print(f"Encoded message: {final}\n")
    elif choice == 3:
        print("Thank you for using the Morse Code Translator")
    else:
        print("Sorry, that was not a valid option")

# I know there has to be a way to make the code below work, but I'm tired lol
# Zombie code
# def encoding(plain_text):
#     translated = ''
#     # plain_text = plain_text.split()
#     for char in plain_text:
#         print(char)
#         morse_letter = encode[char.lower()]
#         if morse_letter == '/':
#             pass
#         else:
#             translated += morse_letter + '/'
#     # plain_text = plain_text.split()
#     # for char in plain_text:
#     # last_char_pos = len(plain_text) - 1
#     # print(f"Last char pos: {last_char_pos}")
#     # print(f"Phrase: {plain_text}")
#     # for i in range(0, len(plain_text)):
#     #     char = plain_text[i]
#     #     print(char)
#     #     # for code in decode.values():
#     #     #     # print(f"Code: {code}")
#     #     #     if code == char.lower():
#     #     #         print(f"Char: {char} Code: {code}")
#     #     #         plain_letter = decode[code]
#     #     #         print(plain_letter)
#     #     #         translated += plain_letter
#     #     print(f"Last pos: {len(plain_text) - 1}, Current pos: {i}, Char: {char}")
#     #     for code, letter in decode.items():
#     #         if code == "/":
#     #             pass
#     #         elif i == last_char_pos:
#     #             translated += code
#     #         elif letter == char:
#     #             translated += code + "/"
#     translated = translated[:-1]
#     return translated