from flask import Flask
from flask_restful import Resource,Api

class equals(Resource): 
	def get(self, number_1, number_2):
		return {'Output': (float(number_1) == float(number_2))}

app = Flask(__name__)
api = Api(app)
api.add_resource(equals, '/<number_1>/<number_2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5058,
		host="0.0.0.0"
	)