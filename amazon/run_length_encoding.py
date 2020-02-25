"""
Given a string, Your task is to  complete the function encode that returns the run length encoded string for the
given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded
and returns the encoded string.
"""


def encode(given_string: str):
    encoded_string = ''
    previous_character = None
    count = 0
    for curent_character in given_string:
        if curent_character == previous_character or not previous_character:
            count += 1
        else:
            encoded_string += previous_character + str(count)
            count = 1
        previous_character = curent_character
    encoded_string += curent_character + str(count)
    return encoded_string


def decode(given_string: str):
    decoded_string = ''
    for i in range(0, len(given_string) - 1, 2):
        decoded_string += given_string[i] * int(given_string[i+1])
    return decoded_string


if __name__ == '__main__':
    print(encode('wwwwaaadexxxxxx'))
    print(decode('w5a3d1e1x6'))