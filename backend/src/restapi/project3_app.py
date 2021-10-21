from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id = 999

project3_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')


@project3_bp.route('/delete/<id>', methods=['GET'])
def deleteProject(id):
    project_json = ProjectApi.delete(id, system_account_id)
    return jsonify(project_json)
