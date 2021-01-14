import string

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet  = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


input_text = input("Enter the words/sentence to encrypt : \n")
print("\n")
print("Here! your encrypted word/senetence : ")
print(caesar(input_text, 8, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
