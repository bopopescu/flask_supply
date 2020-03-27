from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.request import RequestAdapter
from supply_core.use_cases.request import Request
from flask import jsonify
import json


class DeleteRequestAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(DeleteRequestAPI, self).init()

    def get(self, id):
        try:
            bridge = RequestAdapter()
            # access = Request(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)
