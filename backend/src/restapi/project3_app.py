from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import ProjectApi

system_account_id=999

project_bp = Blueprint('project3_app', __name__, url_prefix='/api/project3')
