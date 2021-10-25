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
    assert result_json['body']['updated_by'] == test_operation_account_id
    assert result_json['status']['code'] == "I0001"
    assert result_json['status']['message'] == ""
