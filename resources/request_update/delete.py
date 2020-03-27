from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.request_update import RequestUpdateAdapter
from supply_core.use_cases.request_update import RequestUpdate
from flask import jsonify
import json


class DeleteRequestUpdateAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(DeleteRequestUpdateAPI, self).init()

    def get(self, id):
        try:
            bridge = RequestUpdateAdapter()
            # access = RequestUpdate(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)
