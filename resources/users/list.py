from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.user import UserAdapter
from supply_core.use_cases.users import Users
from flask import jsonify
import json


class ListUsersAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListUsersAPI, self)._init_()

    def get(self):
        try:
            bridge = UserAdapter()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)
