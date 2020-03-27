from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.employee_in_charge import EmployeeInChargeAdapter

from supply_core.use_cases.employee_in_charge import EmployeeInCharge

from flask import jsonify
import json


class ListEmployeeInChargeAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListEmployeeInChargeAPI, self).init()

    def get(self):
        try:
            bridge = EmployeeInChargeAdapter()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)