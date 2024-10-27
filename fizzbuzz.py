#!/usr/bin/env python

def affiche():
	return "".join(
	"FrisBee" if i % 15 == 0 else "Fizz" 
	if i % 3 == 0 else "Buzz" 
	for i in range(1, 101)
		)
print(affiche())

