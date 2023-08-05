from flask import Flask
from flask_restful import Resource,Api

class Modulus(Resource): 
	def get(self, number_1, number_2):
		try:
			return {'Output': (float(number_1) % float(number_2))}
		except: 
			return {'Output': "Modulo by Zero error"}

app = Flask(__name__)
api = Api(app)
api.add_resource(Modulus, '/<number_1>/<number_2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5057,
		host="0.0.0.0"
	)
