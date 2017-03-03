from periodictable import *


def create():
	keyset = []
	for element in elements:
		for other_element in elements:
			if other_element == element:
				continue
			temp = element.symbol + other_element.symbol
			keyset.append(temp)

	keyset = set(keyset)
	return keyset

	
