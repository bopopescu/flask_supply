from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.problem_type import ProblemTypeAdapter

from supply_core.use_cases.problem_types import ProblemTypes
from flask import jsonify
import json


class ListProblemTypeAPI(ResourceBase):
    decorators = [auth.login_required]

    def _init_(self):
        super(ListProblemTypeAPI, self).init()

    def get(self):
        try:
            bridge = ProblemTypeAdapter()
            # access = Department(bridge)
            return jsonify(bridge.list())

        except Exception as e:
            return self.handle_error(e)