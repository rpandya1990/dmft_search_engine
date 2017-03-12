from flask_restful import Resource
from flask import jsonify
from utilities.indexer import index

data = [
	{
		"path": "/var/htmml",
		"last_modified": 1,
		"files": "a.txt b.txt",
		"folders": "var opt",
		"description": "Sample Description"
	}
]

inv_index = index.generate("filesystem.pickle")


class Search(Resource):

	def get(self, keyword=None):
		print len(inv_index)
		return jsonify({"Data": data})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
