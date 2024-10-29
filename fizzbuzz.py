#!/usr/bin/env python

def affiche(n1, n2):
	if not isinstance(n1, int) or not isinstance(n2, int):
		raise ValueError("Les paramètres doivent être des entiers.")
	
	if n1 > n2:
		 raise ValueError("n1 ne doit pas être supérieur à n2.")

	elements = []
	for i in range(n1, n2 + 1):
		if i % 15 == 0:
			elements.append("FrisBee")
		elif i % 3 == 0:
			elements.append("Fizz")
		elif i % 5 == 0:
			elements.append("Buzz")
		else:
			elements.append(str(i))
	return "".join(elements)

print(affiche(5, 10))
print(affiche(10, 16))
