#!/usr/bin/env python

def affiche(n):
	return "".join(
	"FrisBee" if i % 15 == 0 else "Fizz" 
	if i % 3 == 0 else "Buzz" 
	for i in range(1, n+1)
		)
if __name__ == "__main__":
	print(affiche(15))

