from flask import Flask
from flask_restful import Resource,Api

class Division(Resource):
    def get(self,number_1,number_2):
        try:
            return {'Output':(float(number_1)/float(number_2))}
        except: 
            return {'Output': "Division by Zero error"}
    
app=Flask(__name__)
api=Api(app)
api.add_resource(Division, '/<number_1>/<number_2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5055,
		host="0.0.0.0"
	)
