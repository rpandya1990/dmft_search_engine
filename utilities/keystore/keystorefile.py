from periodictable import *


def create():
	"""Generate all keywords.

	Generate keywords which are combinations of 2 elements(symbols)
	and their mapping to names
	Returns:
	    Keyword(combinations of 2 elements) and
	    inverted keyword(mapping of keyword to element names)
	"""
	keyword = {}
	for element in elements:
		for other_element in elements:
			if other_element == element:
				continue
			elements_in_compound = []
			elements_in_compound.append(element.name)
			elements_in_compound.append(other_element.name)
			temp = element.symbol + other_element.symbol
			keyword[temp] = elements_in_compound

	inverted_keyword = {}
	for key, values in keyword.iteritems():
		for item in values:
			if item in inverted_keyword:
				inverted_keyword[item].append(key)
			else:
				inverted_keyword[item] = []
				inverted_keyword[item].append(key)

	return keyword, inverted_keyword
