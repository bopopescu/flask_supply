from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department_country_support import DepartmentCountrySupportAdapter
from supply_core.use_cases.department_country_support import DepartmentCountrySupport
from flask import jsonify
import json


class DeleteDepartmentCountrySupportAPI(ResourceBase):
    decorators = [auth.login_required]

    def init(self):
        super(DeleteDepartmentCountrySupportAPI, self).init()

    def get(self, id):
        try:
            bridge = DepartmentCountrySupportAdapter()
            # access = DepartmentCountrySupport(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)