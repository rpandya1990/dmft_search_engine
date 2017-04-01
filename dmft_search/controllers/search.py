from datetime import datetime
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


class Search(Resource):

	def get(self, keyword=None, showby="DATE"):
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
		    show(None or "Relevance"): Whether search by default(date) or by relevance

		Returns:
		    JSON containing the search results
		"""

		result = []
		print showby

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

		# # Locate compound names with only 2 elements i.e. 1 bigram
		# if len(bigrams) == 1:
		# 	if keyword in inv_index:
		# 		for item in inv_index[keyword].keys():
		# 			data = {}
		# 			data["path"] = item
		# 			data['last_modified'] = filesystem[item]['last_modified']
		# 			data['description'] = "coming soon"
		# 			files = ", ".join(filesystem[item]['files'])
		# 			data['files'] = files
		# 			result.append(data)

	# Locate compund names with more than 2 elements
		if len(bigrams) > 1:
			partial_result = {}
			# Get paths which contain all the bigrams
			superset = []
			for bigram in bigrams:
			    if bigram not in inv_index:
			    	print "Hi"
			        return jsonify({"Data": result})
			    superset.append(inv_index[bigram].keys())
			candidates = set.intersection(*map(set, superset))

			# From the candiates select only those which contain bigrams at adjacent locations
			for candidate in candidates:
			    partial_result[candidate] = []
			    dict1 = {}
			    frequency = 0
			    for key in inv_index[bigrams[0]][candidate].keys():
			        dict1[key] = []
			        # print inv_index[bigrams[0]][candidate][key]
			        present = True
			        for i in xrange(1, len(bigrams)):
			            if key not in inv_index[bigrams[i]][candidate]:
			                present = False
			                break
			        if present is False:
			            continue
			        else:
			            for item in inv_index[bigrams[0]][candidate][key]:
			                flag = True
			                for i in xrange(1, len(bigrams)):
			                    if (item + i) not in inv_index[bigrams[i]][candidate][key]:
			                        flag = False
			                        break
			                if flag is True:
			                    dict1[key].append(item)
			                    frequency += 1

			    if frequency > 0:
			        partial_result[candidate].append((dict1, frequency))

			# Sort the results by relevance or date
			final_result = []

			if showby == "RELEVANCE":
				# Sort the results by relevance by frequency
				for item in partial_result.keys():
					if len(partial_result[item]) > 0:
						#  Parse string to date
						final_result.append((item, partial_result[item][0][1]))
				# Sort final_result by frequency
				final_result = sorted(final_result, key=lambda x: x[1])[::-1]

			if showby == "DATE":
				# Order by most recently modified
				for item in partial_result.keys():
					if len(partial_result[item]) > 0:
						#  Parse string to date
						final_result.append((item, datetime.strptime(filesystem[item]['last_modified'], '%a %b %d %H:%M:%S %Y')))
				# Sort final_result by date
				final_result = sorted(final_result, key=lambda x: x[1])[::-1]

			print final_result

			for item in final_result:
				data = {}
				data["path"] = item[0]
				data['last_modified'] = filesystem[item[0]]['last_modified']
				data['description'] = "coming soon"
				files = ", ".join(filesystem[item[0]]['files'])
				data['files'] = files
				result.append(data)

		return jsonify({"Data": result})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
