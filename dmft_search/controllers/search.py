from flask_restful import Resource
from flask import jsonify


data = [
	{
		"owner": 1,
		"id": 1,
		"path": "Hello tirl",
		"description": "m rerum est autem sunt rem eveniet architecto"
	},
	{
		"owner": 1,
		"id": 2,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	}
]


class Search(Resource):

	def get(self, keyword=None):
		return jsonify({"Data": data})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
