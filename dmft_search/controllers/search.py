import pickle
from datetime import datetime
from flask_restful import Resource
from flask import jsonify

# data = [
# 	{
# 		"path": "/var/htmml",
# 		"last_modified": 1,
# 		"files": "a.txt b.txt",
# 		"folders": "var opt",
# 		"description": "Sample Description"
# 	}
# ]


class Search(Resource):
	def __init__(self):
		with open('dmft_search/files/filesystem/filesystem.pickle', 'rb') as handle:
			self.filesystem = pickle.load(handle)
		with open('dmft_search/files/index/Index.pickle', 'rb') as handle1:
			self.invindex = pickle.load(handle1)

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
		print "Searching by: " + showby

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
		print elem_in_compound
		for i in xrange(len(elem_in_compound) - 1):
			bigrams.append(elem_in_compound[i] + elem_in_compound[i + 1])

		# # Locate compound names with only 2 elements i.e. 1 bigram
		# if len(bigrams) == 1:
		# 	if keyword in self.invindex:
		# 		for item in self.invindex[keyword].keys():
		# 			data = {}
		# 			data["path"] = item
		# 			data['last_modified'] = self.filesystem[item]['last_modified']
		# 			data['description'] = "coming soon"
		# 			files = ", ".join(self.filesystem[item]['files'])
		# 			data['files'] = files
		# 			result.append(data)

	# Locate compund names with more than 2 elements
		if len(bigrams) > 1:
			partial_result = {}
			# Get paths which contain all the bigrams
			superset = []
			for bigram in bigrams:
			    if bigram not in self.invindex:
			    	print bigram
			    	print "Not in inv index"
			        return jsonify({"Data": result})
			    superset.append(self.invindex[bigram].keys())
			candidates = set.intersection(*map(set, superset))

			print "Initial candidates: " + str(candidates)

			# From the candiates select only those which contain bigrams at adjacent locations
			for candidate in candidates:
			    partial_result[candidate] = []
			    dict1 = {}
			    frequency = 0
			    for key in self.invindex[bigrams[0]][candidate].keys():
			        dict1[key] = []
			        # print self.invindex[bigrams[0]][candidate][key]
			        present = True
			        for i in xrange(1, len(bigrams)):
			            if key not in self.invindex[bigrams[i]][candidate]:
			                present = False
			                break
			        if present is False:
			            continue
			        else:
			            for item in self.invindex[bigrams[0]][candidate][key]:
			                flag = True
			                for i in xrange(1, len(bigrams)):
			                    if (item + len(elem_in_compound[i - 1])) not in self.invindex[bigrams[i]][candidate][key]:
			                        flag = False
			                        break
			                if flag is True:
			                    dict1[key].append(item)
			                    frequency += 1

			    if frequency > 0:
			        partial_result[candidate].append((dict1, frequency))

			# print "Unranked/Unsorted Result: " + str(partial_result)

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
						final_result.append((item, datetime.strptime(self.filesystem[item]['last_modified'], '%a %b %d %H:%M:%S %Y')))
				# Sort final_result by date
				final_result = sorted(final_result, key=lambda x: x[1])[::-1]

			print final_result

			for item in final_result:
				data = {}
				data["path"] = item[0]
				data['last_modified'] = self.filesystem[item[0]]['last_modified']
				data['description'] = "coming soon"
				files = ", ".join(self.filesystem[item[0]]['files'])
				data['files'] = files
				result.append(data)

		return jsonify({"Data": result})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
