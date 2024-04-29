from . import examination
from . import processing
from . import frequency_analysis as fa
from . import SPANISH_DICT as SPANISH_DICT
from .const import *
from . import EN_REL_FREQ
import string




def _decypher(cyphertext, key):
    letters = string.ascii_uppercase
    #letters = SPANISH_DICT
    shifts = [letters.index(letter) for letter in key]
    blocks = processing.get_blocks(text=cyphertext,size=len(key))
    cols = processing.get_columns(blocks)
    decyphered_blocks = processing.to_blocks([fa.shift(col, shift) for col, shift in zip(cols, shifts)])
    decyphered = ''.join(decyphered_blocks)
    return decyphered


def attack(file):
    with open(file) as f:
        cyphertext = f.readlines()
        key_len = 0
        key_len = examination.estimateKeyLength(cyphertext[0])
        key = fa.restore_key(cyphertext[0], key_len)
        decyphered = _decypher(cyphertext[0], key)
        frequencies = fa._get_letter_frequencies(text=decyphered)
        print('Chosen key length: '+str(key_len))
        print('Restored key: '+str(key))
        print('Plaintext: '+str(decyphered))


