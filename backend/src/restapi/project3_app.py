from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id = 999

project3_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')


@project3_bp.route('/update', methods=['POST'])
def updateProject():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = ProjectApi.update(payload)
    return jsonify(response_json)


@project3_bp.route('/update_for_lock', methods=['POST'])
def updateProjectWithLock():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = ProjectApi.updateWithLock(payload)
    return jsonify(response_json)
