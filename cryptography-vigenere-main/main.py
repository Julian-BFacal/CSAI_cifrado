from vigenere_cipher.attacking import attack

from functools import reduce

'''
DEMO VIGENERE CIPHER
    1. plaintext, key --> VigenereCipher() --> ciphertext
    2. ciphertext --> Kasiski method --> key length
    3. ciphertext, key length --> cryptanalysis --> plaintext
'''

def main():
    # load the test data
    file = 'JdP_002_input'
    print(">> [SYSTEM] Loading test text")
    with open(file) as f:
        text = f.readlines()
    # kasiski exam
    print('\n>> [SYSTEM] Start attacking with Kasiski examination......')
    attack(file)


if __name__ == '__main__':
    main()


