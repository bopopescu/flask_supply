from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.request import RequestAdapter
from supply_core.use_cases.support_department import SupportDepartment
from flask import jsonify
import json


class GetRequestUser(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(GetRequestUser, self).init()

    def get(self, mail):
        try:
            bridge = RequestAdapter()
            # access = Department(bridge)
            return jsonify(bridge.getRequestUser(mail))

        except Exception as e:
            return self.handle_error(e)
