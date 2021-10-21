from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id = 999

project3_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')


@project3_bp.route('/get/<id>', methods=['GET'])
def getProject(id):
    project_json = ProjectApi.getById(id, system_account_id)
    return jsonify(project_json)


@project3_bp.route('/lock', methods=['POST'])
def lockAccount():
    payload = request.json
    print(f"account_app#lockAccount() payload={payload}")
    project_json = ProjectApi.getByIdWithLock(payload)
    return jsonify(project_json)
    # TODO lockする場合はロックするユーザーidも渡す必要がある。POSTへの変更が望ましい。
