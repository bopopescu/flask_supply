from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department_country_support import DepartmentCountrySupportAdapter
import json


class NewDepartmentCountrySupportAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(NewDepartmentCountrySupportAPI, self).init()

    def post(self):
        try:
            data = request.data.decode()
            json_data = json.loads(data)
            json_data['method'] = "post"
            print(json_data)
            bridge = DepartmentCountrySupportAdapter()
            return bridge.new(json_data)
        except Exception as e:
            return self.handle_error(e)