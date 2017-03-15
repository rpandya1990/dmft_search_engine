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

inv_index, filesystem = index.generate("filesystem.pickle")  # Hardcoded for now


class Search(Resource):

	def get(self, keyword=None):
		result = []
		if keyword in inv_index:
			for item in inv_index[keyword]:
				data = {}
				data["path"] = item
				data['last_modified'] = filesystem[item]['last_modified']
				data['description'] = "coming soon"
				files = ", ".join(filesystem[item]['files'])
				folders = ", ".join(filesystem[item]['folders'])
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
