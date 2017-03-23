from flask_restful import Resource
from flask import jsonify
from utilities.indexer import index

# data = [
# 	{
# 		"path": "/var/htmml",
# 		"last_modified": 1,
# 		"files": "a.txt b.txt",
# 		"folders": "var opt",
# 		"description": "Sample Description"
# 	}
# ]

# Hardcoded for now
inv_index, filesystem = index.generate("filesystem.pickle")
print filesystem


class Search(Resource):

	def get(self, keyword=None):
		"""Return the path which may contain the compound keyword.

		Note: Locate compound names with 2 or more elements

		For compound with only 2 elements:

		For compound with 3 or more elements i.e. more than 1 bigram:
			Get all folders whose path contains all the bigrams
			A path has high probability of containing the compound name
			if bigrams are present in the adjancent index of the
			filtered path(digits removed)
			For eg: Path: /Ni2Ag3O2
					After filtering: /NiAgO
					NiAg present at index 0
					AgO present at index 1
		Args:
		    keyword: Compound name(Element should start with uppercase)
		    For example: Fe2O3, CO2, H2SO4 are valid, co2, fe2o3 are not valid

		Returns:
		    JSON containing the search results
		"""

		result = []

		# Filter the keyword to form multiple bigrams
		elem_in_compound = []
		bigrams = []
		temp = ''
		for character in keyword:
		    if character.isdigit():
		    	continue
		    if len(temp) > 0 and character.isupper():
		    	elem_in_compound.append(temp)
		    	temp = ''
		    temp = temp + character
		elem_in_compound.append(temp)
		for i in xrange(len(elem_in_compound) - 1):
			bigrams.append(elem_in_compound[i] + elem_in_compound[i + 1])

		# Locate compound names with only 2 elements i.e. 1 bigram
		if len(bigrams) == 1:
			if keyword in inv_index:
				for item in inv_index[keyword]:
					data = {}
					data["path"] = item[0]
					data['last_modified'] = filesystem[item[0]]['last_modified']
					data['description'] = "coming soon"
					files = ", ".join(filesystem[item[0]]['files'])
					folders = ", ".join(filesystem[item[0]]['folders'])
					data['files'] = files
					data['folders'] = folders
					result.append(data)

		return jsonify({"Data": result})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
