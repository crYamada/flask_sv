from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id = 999

project3_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')

@project3_bp.route('/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = ProjectApi.getById(id, system_account_id)
    return jsonify(account_json)
