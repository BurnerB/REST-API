from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from Resources.userEndpoints import UserRegister
from Resources.ItemEndpoints import Item,ItemList

app = Flask(__name__)
api = Api(app)
app.secret_key = "BABA"

jwt = JWT(app,authenticate,identity) # /auth


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister,"/register")

if __name__ == "__main__":
    app.run(port=5000, debug =True)
