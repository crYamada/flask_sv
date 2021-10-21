from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id = 999

project3_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')


@project3_bp.route('/create', methods=['POST'])
def createProject():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = ProjectApi.create(payload)
    return jsonify(response_json)
