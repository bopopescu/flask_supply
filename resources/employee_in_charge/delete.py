from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.employee_in_charge import EmployeeInChargeAdapter
from supply_core.use_cases.employee_in_charge import EmployeeInCharge
from flask import jsonify
import json


class DeleteEmployeeInChargeAPI(ResourceBase):
    decorators = [auth.login_required]

    def init(self):
        super(DeleteEmployeeInChargeAPI, self).init()

    def get(self, id):
        try:
            bridge = EmployeeInChargeAdapter()
            # access = EmployeeInCharge(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)