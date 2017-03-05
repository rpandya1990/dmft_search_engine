from flask import Flask
from flask_restful import Api
from flask import render_template
from controllers import search
app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(search.Search, '/search/<string:keyword>')


if __name__ == '__main__':
    app.run(debug=True)
