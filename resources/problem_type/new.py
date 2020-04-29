from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.problem_type import ProblemTypeAdapter
import json


class NewProblemTypesAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(NewProblemTypesAPI, self).init()

    def post(self):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = ProblemTypeAdapter()
            return bridge.new(json_data)
        except Exception as e:
            return self.handle_error(e)