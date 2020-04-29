from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.request_update import RequestUpdateAdapter
from supply_core.use_cases.request_update import RequestUpdate
from flask import jsonify
import json


class UpdateRequestUpdateAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(UpdateRequestUpdateAPI, self).init()

    def post(self, id):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = RequestUpdateAdapter()
            return bridge.update(id, json_data)

        except Exception as e:
            return self.handle_error(e)
