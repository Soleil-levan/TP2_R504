#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fizzbuzz import affiche 

def test_affiche_n():
	result = affiche(15)
	expected = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
	assert result == expected, f"Expected {expected}, but got {result}"

def test_affiche_n_limiter():
	result = affiche(5)
	expected = "12Fizz4Buzz"
	assert result == expected, f"Expected {expected}, but got {result}"

	result = affiche(1)
	expected = "1"
	assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == " __main__":
	test_affiche_n()
	test_affiche_n_limiter()
print("All tests passed")


