from http import HTTPStatus

from flask import request
from flask_restful import Resource

from db.helper import DBHelper
from utils.utils import Shows


class ShowsResource(Resource):
    def get(self):
        return DBHelper.run_query(Shows.get_shows_query()), HTTPStatus.OK
    
    def post(self):
        body = request.get_json(force=True)
        try:
            DBHelper.run_query(Shows.post_show_query(body))
            return { "msg" : "Creating show operation successful." }, HTTPStatus.OK
        except Exception:
            return { "msg" : "Creating show operation FAILED!!!" }, HTTPStatus.BAD_REQUEST

    def patch(self):
        body = request.get_json(force=True)
        try:
            DBHelper.run_query(Shows.update_show_query(body))
            return { "msg" : "Creating show operation successful." }, HTTPStatus.OK
        except Exception:
            return { "msg" : "Creating show operation FAILED!!!" }, HTTPStatus.BAD_REQUEST
    
    def delete(self):
        try:
            body = request.get_json(force=True)            
            DBHelper.run_query(Shows.delete_show_query(body))
            return { "msg" : "Deleting show operation successful." }, HTTPStatus.OK
        except Exception:
            return { "msg" : "Deleting show operation FAILED!!!" }, HTTPStatus.BAD_REQUEST

