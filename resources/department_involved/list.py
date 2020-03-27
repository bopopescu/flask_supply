from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department_involved import DepartmentInvolvedAdapter
from supply_core.use_cases.departments_involved import DepartmentsInvolved
from flask import jsonify
import json


class ListDepartmentInvolvedAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListDepartmentInvolvedAPI, self).init()

    def get(self):
        try:
            bridge = DepartmentInvolvedAdapter()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)
