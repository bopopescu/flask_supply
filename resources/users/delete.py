from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.user import UserAdapter
from supply_core.use_cases.users import Users
from flask import jsonify
import json


class DeleteUserAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(DeleteUserAPI, self)._init_()

    def get(self, id):
        try:
            bridge = UserAdapter()
            # access = Users(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)
