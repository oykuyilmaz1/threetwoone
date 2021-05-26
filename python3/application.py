from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from db.helper import DBHelper
from core.shows import ShowsResource

application = Flask(__name__)
cors = CORS(application)
application.config.from_object('config.Config')

DBHelper.init_app(application)

api = Api(application)

api.add_resource(ShowsResource, "/show")

if __name__ == "__main__":
    application.run(host="127.0.0.1", port=5001)
