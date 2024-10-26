from fizzbuzz import affiche 

def test_affiche():
	result = affiche()
	assert "Fizz" in result, "Fizz devrait app"
	assert "Buzz" in result, "Buzz devraot app"
	assert "FrisBee" in result, "FrisBee deavrit app"
