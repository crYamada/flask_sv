from model import db
from model import Project
from model import Status
from restapi import ProjectApi
import json
import pprint
import datetime
import ujson
import requests
import pytest
from model.common import strftime
from model.common import strptime


def test_project_get():
    """
    restapi/getById
    """
    project = {
        'project_name': 'flask_sv',
        'description': 'test of getById',
        'status': 0,
        'creater_id': 999,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 999,
        'updated_at': '2021-12-31 00:00:00'
    }

    Project.create(project, 999) == True

    project_dict = {
        'project_name': "flask_sv",
        'status': 0
    }
    result = Project.search(project_dict, 1)
    project_id = result[0].id

    # APIから確認
    url = f"http://localhost:5000/api/project3/get/{project_id}"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    data = json.loads(response.text)
    assert data['body']['project_name'] == project['project_name']
    assert data['body']['description'] == project['description']
    assert data['body']['status'] == project['status']
    assert data['body']['created_by'] == project['creater_id']
    # assert data['body']['created_at'] == project['created_at']
    assert data['body']['last_updated_by'] == project['updater_id']
    # assert data['body']['last_updated_at'] == project['updated_at']
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == ""


def test_project_create():
    """
    """
    # modelから試験データ登録
    test_project_name = 'api_project_get'
    test_description = 'test of create api'
    test_status = 0
    test_operation_account_id = 997
    payload = {
        'project_name': test_project_name,
        'description': test_description,
        'status': test_status,
        'operation_account_id': test_operation_account_id
    }

    # createのテスト
    # APIの実行
    url = f"http://localhost:5000/api/project3/create"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 200
    data = json.loads(response.text)
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Creating project was successfully."

    # 作成されたデータの確認
    project_dict = {
        'project_name': test_project_name,
        'status': test_status
    }
    result = Project.search(project_dict, 999)
    project_id = result[0].id

    result_json = ProjectApi.getById(project_id, 100)
    print(f"result_json:{result_json}")
    assert result_json['body']['project_name'] == test_project_name
    assert result_json['body']['description'] == test_description
    assert result_json['body']['status'] == test_status
    assert result_json['body']['created_by'] == test_operation_account_id
    assert result_json['body']['last_updated_by'] == test_operation_account_id
    assert result_json['status']['code'] == "I0001"
    assert result_json['status']['message'] == ""


def test_project_search():
    """
    """
    operation_account_id = 996
    project = {
        'project_name': 'search_project',
        'description': 'test of search api',
        'status': 0,
        'creater_id': 200,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 200,
        'updated_at': '2021-12-31 00:00:00'
    }

    # createのテスト
    assert Project.create(project, 999) == True

    payload = {
        "project_name": "search_project",
        "creater_id": 200,
        "operation_account_id": operation_account_id
    }
    #result = Project.search(query, 999)

    # APIから確認
    url = f"http://localhost:5000/api/project3/search"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    # HTTP Statusコードが200であること
    assert response.status_code == 200

    print(f"test_project_search():json response.text={response.text}")
    # BODYをjsonでパースできること
    data = json.loads(response.text)
    print(f"test_account_search():json data={data}")
    assert data['body'][0]['project_name'] == payload['project_name']
    assert data['body'][0]['creater_id'] == project['creater_id']
    assert data['body'][0]['status'] == project['status']
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Found (1) records."


def test_project_update():
    """
    """
    project = {
        'project_name': 'update_project',
        'description': 'test of update api',
        'status': 0,
        'creater_id': 700,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 700,
        'updated_at': '2021-12-31 00:00:00'
    }
    operation_account_id = 998
    # create
    assert Project.create(project, 700) == True

    search_query = {
        'project_name': 'update_project',
        'status': 0,
        'creater_id': 700
    }
    result = Project.search(search_query, 999)

    assert result[0].project_name == project['project_name']

    project_id = result[0].id
    payload = {
        'id': project_id,
        'project_name': 'update_project_modified',
        'status': 2,
        'operation_account_id': str(operation_account_id)
    }

    # APIから確認
    url = f"http://localhost:5000/api/project3/update"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    # HTTP Statusコードが200であること
    assert response.status_code == 200

    data = json.loads(response.text)
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Updating project was successfully."

    search_query = {
        'project_name': 'update_project_modified',
    }
    result = Project.search(search_query, 999)
    assert result[0].creater_id == project['creater_id']
    assert result[0].updater_id == operation_account_id
    assert result[0].status == payload['status']


def test_project_update_with_lock():
    """
    """
    project = {
        'project_name': 'update_project_lock',
        'description': 'test of update_for_lock api',
        'status': 0,
        'creater_id': 701,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 701,
        'updated_at': '2021-12-31 00:00:00'
    }

    operation_account_id = 998
    # create
    Project.create(project, 999) == True

    search_query = {
        'project_name': 'update_project_lock',
        'status': 0,
        'creater_id': 701
    }
    result = Project.search(search_query, 999)
    assert result[0].project_name == project['project_name']
    project_id = result[0].id

    payload = {
        'id': project_id,
        'operation_account_id': operation_account_id
    }

    # APIから検索しロックをする
    url = f"http://localhost:5000/api/project3/lock"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)
    print(f"lock:{response}")
    assert response.status_code == 200

    data = json.loads(response.text)
    print(f"data={data}")
    assert data['body']['id'] == project_id
    assert data['body']['project_name'] == project['project_name']
    assert data['body']['description'] == project['description']
    assert data['body']['status'] == project['status']
    assert data['body']['created_by'] == project['creater_id']
    assert data['body']['last_updated_by'] == project['updater_id']
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == ""

    # TODO ロックしたレコードを更新しようとするとロックされることを数秒間応答がないことで確認する

    payload = {
        'id': project_id,
        'project_name': 'update_project_lock2',
        'status': 2,
        'operation_account_id': operation_account_id
    }

    # ロックしたレコードを更新する
    url = f"http://localhost:5000/api/project3/update_for_lock"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    # HTTP Statusコードが200であること
    print(f"update_lock:{response}")
    assert response.status_code == 200
    data = json.loads(response.text)
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Updating project was successfully."

    search_query = {
        'project_name': 'update_account_lock2',
    }
    result = Project.search(search_query, 999)
    assert result[0].project_name == payload['project_name']
    assert result[0].creater_id == project['creater_id']
    assert result[0].updater_id == operation_account_id
    assert result[0].status == payload['status']


def test_project_delete():
    """
    """
    project = {
        'project_name': 'delete_project',
        'description': 'test of delete api',
        'status': 0,
        'creater_id': 702,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 702,
        'updated_at': '2021-12-31 00:00:00'
    }

    # create
    Project.create(project, 999) == True

    search_query = {
        'project_name': 'delete_project',
        'status': 0,
        'creater_id': 702
    }
    result = Project.search(search_query, 999)
    assert result[0].project_name == project['project_name']
    account_id = result[0].id

    # APIから確認
    url = f"http://localhost:5000/api/project3/delete/{account_id}"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.get(url, headers=headers)

    # HTTP Statusコードが200であること
    assert response.status_code == 200

    data = json.loads(response.text)
    print(
        f"test_ProjectApi#test_project_delete data={data} code={data['status']['code']} message={data['status']['message']}")
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Deleting project was successfully."
