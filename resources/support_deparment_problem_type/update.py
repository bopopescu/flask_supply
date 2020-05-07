from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.support_department_problem_type import SupportDepartmentProblemType
from supply_core.use_cases.support_department import SupportDepartment
from flask import jsonify
import json


class UpdateSupportDepartmentProblemTypeAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(UpdateSupportDepartmentProblemTypeAPI, self).init()

    def post(self, id):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = SupportDepartmentProblemType()
            return bridge.update(id, json_data)

        except Exception as e:
            return self.handle_error(e)
