def function(x):
	return x * 2

def test_positivo():
	assert function(2) == 4

def test_zero():
	assert function(0) == 0

def test_negativo():
	assert function(-2) == -4