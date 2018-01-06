from flask_restful import Resource, reqparse
from models.store_model import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'Stores': store.json()}
       
        return {"message": "Store with this name already exist"}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"message": "Store with {} name already exist".format(name)}, 404
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                 return {"Message":"There was an error, please try again"}, 500
        
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            
        return {"Message":"Store deleted"}



class StoreList(Resource):
    def get(self):
        return {"Stores": [store.json() for store in StoreModel.query.all()]}