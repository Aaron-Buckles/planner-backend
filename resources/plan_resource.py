from flask import request
from flask_restful import Resource
from webargs.flaskparser import parser

import utils.db as db
import utils.messages as msg
from models.plan_model import PlanModel


class PlanResource(Resource):
    def get(self, name):
        term = request.args.get("term")

        try:
            if term:
                plans = db.find_by(PlanModel, name=name, term=term)
            else:
                plans = db.find_by(PlanModel, name=name)
        except:
            return {"message": msg.internal_server("retrieve", "Plan")}, 500

        if plans:
            return {"plans": [plan.json() for plan in plans]}
        else:
            return {"message": msg.not_found("Plan", (name, args))}, 404

    def post(self, name):
        args = parser.parse(PlanSchema, request)

        plan = PlanModel(name=name, **args)
        try:
            db.save(plan)
        except:
            return {"message": msg.internal_server("save", "PlanModel")}, 500

        return {"message": msg.success("Plan", "created"), "plan": plan.json()}, 201
