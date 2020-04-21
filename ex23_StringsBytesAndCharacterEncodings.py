# Exercise 23: Strings, Bytes and Character Encodings

import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        # Recursive call
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # It's a string with trailing "\n" removed
    next_lang = line.strip()  
    # encoding string to bytes
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # decoding bytes to string
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    print(raw_bytes, "<===>", cooked_string)

languages = open('ex23_languages.txt', encoding='utf-8')

main(languages, encoding, error)
