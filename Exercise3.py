#Caesar Cipher input plaintext and number of shifts for encrypted message
def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def sameAmount(S, word1, word2):
    if S.count(word1) == S.count(word2):
        return True
    else:
        return False
