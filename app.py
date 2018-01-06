from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UsersRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Mahmoud'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UsersRegister, "/signup")
api.add_resource(Store, '/store/<name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)