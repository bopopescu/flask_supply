from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.request import RequestAdapter
from supply_core.use_cases.request import Request
from flask import jsonify
import json


class NewRequestAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(NewRequestAPI, self).init()

    def post(self):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = RequestAdapter()
            return bridge.new(json_data)
        except Exception as e:
            return self.handle_error(e)
