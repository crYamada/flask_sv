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


@project3_bp.route('/create', methods=['POST'])
def createProject():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = ProjectApi.create(payload)
    return jsonify(response_json)


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


@project3_bp.route('/search', methods=['POST'])
def searchProject():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = ProjectApi.search(payload)
    return jsonify(response_json)


@project3_bp.route('/delete/<id>', methods=['GET'])
def deleteProject(id):
    project_json = ProjectApi.delete(id, system_account_id)
    return jsonify(project_json)
