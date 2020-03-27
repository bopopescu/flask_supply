from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.department import DepartmentAdapter

from supply_core.use_cases.department import Department
from flask import jsonify
import json


class DeleteDepartmentAPI(ResourceBase):
    decorators = [auth.login_required]

    def init(self):
        super(DeleteDepartmentAPI, self).init()

    def get(self, id):
        try:
            bridge = DepartmentAdapter()
            # access = Department(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)