import string


def is_pangram(s):

    s = ''.join(filter(str.isalpha, s.lower()))
    letters_in_string = set(s)
    return set(string.ascii_lowercase) <= letters_in_string


input_string = "The quick brown fox jumps over the lazy dog"

if is_pangram(input_string):
    print(f"'{input_string}' is a pangram.")
else:
    print(f"'{input_string}' is not a pangram.")
