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
	},
	{
		"owner": 1,
		"id": 3,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 4,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 5,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 6,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 7,
		"path": "Hello tirl",
		"description": "m rerum est autem sunt rem eveniet architecto"
	},
	{
		"owner": 1,
		"id": 8,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 9,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 10,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 11,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	},
	{
		"owner": 1,
		"id": 12,
		"path": "/var/html/raghav",
		"description": "Crated using dfmmt"
	}
]


class Search(Resource):

	def get(self, keyword=None):
		print keyword
		return jsonify({"Data": data})

	def post(self):
		return None

	def put(self):
		return None

	def delete(self):
		return None
