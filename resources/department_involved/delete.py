from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department_involved import DepartmentInvolvedAdapter
from supply_core.use_cases.departments_involved import DepartmentsInvolved
from flask import jsonify
import json


class DeleteDepartmentsInvolvedAPI(ResourceBase):
    decorators = [auth.login_required]

    def init(self):
        super(DeleteDepartmentsInvolvedAPI, self).init()

    def get(self, id):
        try:
            bridge = DepartmentInvolvedAdapter()
            # access = DepartmentsInvolved(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)