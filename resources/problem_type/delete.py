from flask_restful import fields, marshal
from flask import make_response
from flask import request
from common.auth import auth
from resources.resource_base import ResourceBase
from TechTeam.adapter.problem_type import ProblemTypeAdapter
from supply_core.use_cases.problem_types import ProblemTypes
from flask import jsonify
import json

class DeleteProblemTypesAPI(ResourceBase):
    decorators = [auth.login_required]

    def init(self):
        super(DeleteProblemTypesAPI, self).init()

    def get(self, id):
        try:
            bridge = ProblemTypeAdapter()
            # access = ProblemTypes(bridge)
            return jsonify(bridge.delete(str(id)))

        except Exception as e:
            return self.handle_error(e)