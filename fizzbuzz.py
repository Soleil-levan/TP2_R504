#!/usr/bin/env python

def affiche():
	elements = []
	for i in range (1, 101):
		if i % 15 == 0:
			elements.append("frisBee")
		elif i % 3 ==0:
			elements.append("Fizz")	
		elif i % 5 == 0:
		 elements.append("Buzz")
		else:
		 elements.append(str(i))
	return "".join(elements)		

print(affiche())
