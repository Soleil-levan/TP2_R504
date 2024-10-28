#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fizzbuzz import affiche 

def test_affiche_n1_n2():
	result = affiche(5, 10)
	expected = "BuzzFizz78FizzBuzz"
	assert result == expected, f"Expected {expected}, but got {result}"

	result = affiche(10, 16)
	expected = "12Fizz4Buzz11Fizz1314FrisBee16"
	assert result == expected, f"Expected {expected}, but got {result}"

	result = affiche(1, 1)
	expected = "1"
	assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == " __main__":
	test_affiche_n1_n2()
	print("All tests passed")


