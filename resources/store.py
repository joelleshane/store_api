from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json() #,200 status code is default so we don't need to add it
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if Store.Model.find_by_name(name):
            return {'message': "A store with name '{}' exsists already.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'}, 500 #not sure what error was

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # [store.json() for store in StoreModel.qyer]
