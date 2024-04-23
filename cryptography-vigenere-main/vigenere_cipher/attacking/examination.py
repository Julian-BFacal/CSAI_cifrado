# KASISKI METHOD

from functools import reduce
import sys
#sys.path.append('cryptography-vigenere/vigenere_cipher/attacking')
from . import ic

def gcd_2_helper(a: int, b: int) -> int:
	if a == 0:
		return b
	return gcd_2_helper(b % a, a)

def gcd_n(numbers: list) -> int:
	if len(numbers) == 0:
		return 1
	numbers = list(numbers)
	numbers.sort()
	return reduce(gcd_2_helper, numbers)

def kasiski(encrypted_text: str, str_size: int) -> int:
	str_bin = {}
	for i in range(len(encrypted_text)-str_size):
		str_ngram = encrypted_text[i:i+str_size]
		if str_ngram in str_bin:
			str_bin[str_ngram].append(i)
		else:
			str_bin[str_ngram] = [i]

	distance_set = set()
	for ngram_distances in str_bin:
		for i in range(len(str_bin[ngram_distances])):
			for j in range(i+1, len(str_bin[ngram_distances])):
				distance_set.add(str_bin[ngram_distances][j] - str_bin[ngram_distances][i])
	
	return gcd_n(distance_set)

def estimateKeyLength(encrypted_text: str) -> int:
	key_length_candidates = set()
	ngram_size_list = [3, 4, 5, 6, 7]
	for ngram_size in ngram_size_list:
		key_length_candidates.add(kasiski(encrypted_text, ngram_size))
		# print(kasiski(encrypted_text, ngram_size))

	best_key_length = None
	best_key_len_diff = ic.ic_english
	for key_length in key_length_candidates:
		ic_key_length = ic.index_of_coincidence(encrypted_text, key_length)
		ic_key_length_diff =  abs(ic.ic_english - ic_key_length)
		if best_key_len_diff > ic_key_length_diff:
			best_key_len_diff = ic_key_length_diff
			best_key_length = key_length
	if best_key_length != None:
		return best_key_length
	else: 
		return 1
