import sumTwoNumbers
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Stations(Resource):
    def get(self, location):
        return {'The list of police stations are': sumTwoNumbers.police(location)}


api.add_resource(Stations, '/policestations/<location>')

if __name__ == '__main__':
    app.run()