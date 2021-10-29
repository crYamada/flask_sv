from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from restapi import AccountApi

system_account_id = 999

account_bp = Blueprint('account_app', __name__, url_prefix='/api/account')


@account_bp.route('/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = AccountApi.getById(id, system_account_id)
    res = make_response(jsonify(account_json))
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080/"
    res.headers['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
    res.headers['Access-Control-Max-Age'] = 17280000
    res.headers['Access-Control-Allow-Headers'] = "*"
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Credentials'] = "true"
    return res


@account_bp.route('/lock', methods=['POST'])
def lockAccount():
    payload = request.json
    print(f"account_app#lockAccount() payload={payload}")
    account_json = AccountApi.getByIdWithLock(payload)
    return jsonify(account_json)
    # TODO lockする場合はロックするユーザーidも渡す必要がある。POSTへの変更が望ましい。


@account_bp.route('/create', methods=['POST'])
def createAccount():
    payload = request.get_json()
    print(f"api createAccount payload={payload}")
    response_json = AccountApi.create(payload)
    res = make_response(jsonify(response_json))
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080"
    res.headers['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
    res.headers['Access-Control-Max-Age'] = 17280000
    res.headers['Access-Control-Allow-Headers'] = "*"
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Credentials'] = "true"
    return res


@account_bp.route('/search', methods=['POST'])
def searchAccount():
    print(
        f"api searchAccount requestjson={request.get_json(force=True)} data={request.form} encode={request.data.decode('utf-8')}")
    payload = request.get_json()
    print(f"api searchAccount payload={payload}")
    response_json = AccountApi.search(payload)
    res = make_response(jsonify(response_json))
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080"
    res.headers['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
    res.headers['Access-Control-Max-Age'] = 17280000
    res.headers['Access-Control-Allow-Headers'] = "*"
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Credentials'] = "true"
    return res


@account_bp.route('/search_range', methods=['POST'])
def searchRangeAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.search_range(payload)
    return jsonify(response_json)


@account_bp.route('/update', methods=['POST'])
def updateAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.update(payload)
    return jsonify(response_json)


@account_bp.route('/update_for_lock', methods=['POST'])
def updateAccountWithLock():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.updateWithLock(payload)
    return jsonify(response_json)


@account_bp.route('/delete/<id>', methods=['GET'])
def deleteAccount(id):
    account_json = AccountApi.delete(id, system_account_id)
    return jsonify(account_json)


class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}


api = Api(account_bp)
api.add_resource(Spam, '/spam')
