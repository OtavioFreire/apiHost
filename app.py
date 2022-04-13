from flask import Flask,Response
from flask_restx import Api, Resource
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://redadmin:1234@cluster0.euics.mongodb.net/ApiTest?retryWrites=true&w=majority"

api = Api(app)
mongo = PyMongo(app)

ns_perfil = api.namespace('Perfil',
                            description='Descrição da Categoria')

@ns_perfil.route('')
class HelloWorld(Resource):

    def get(self):
        '''
            Retorna todos os perfis no banco de dados
        '''
        users = mongo.db.Perfil.find()
      
        resp = json_util.dumps(users)

        return Response(resp, mimetype='application/json')

    def post(self):
        pass
if __name__ == "__main__":
    app.run(debug=True)
