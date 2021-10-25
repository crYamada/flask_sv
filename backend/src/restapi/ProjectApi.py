from model import Project
from model import Status
#from __future__ import absolute_import, unicode_literals
import json
import datetime
from model.common import strftime
from model.common import strptime

#import requests


def getById(project_id, operation_account_id):
    """
    /project3/get/<id>で呼び出されたAPIの検索処理

    Parameters
    ----------
    project_id : int
        検索するプロジェクトのプロジェクトID
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    ret
        json形式のプロジェクト詳細
    {
        "body": {
            "project_name": <project_name>,
            "description": <description>,
            "status": <status>,
            "created_by": <creater_id>,
            "created_at": <created_at>,
            "last_updated_by": <updater_id>,
            "last_updated_at": <update_at>
        },
        "status": {
            "code" : "I0001",
            "message" : "",
            "detail" : ""
        }
    }
    """

    result = Project.getById(project_id, operation_account_id)
    print(f"ProjectApi#getById result={result}")
    print(f"ProjectApi#getById result.creater_id={result.creater_id}")
    print(f"ProjectApi#getById result.created_at={result.created_at}")
    print(f"ProjectApi#getById result.updater_id={result.updater_id}")
    print(f"ProjectApi#getById result.updated_at={result.updated_at}")
    # TODO モデルの検索結果(正常・異常)によってレスポンスの出力内容を変える
    result_json = {
        "body": {
            "id": project_id,
            "project_name": result.project_name,
            "description": result.description,
            "status":  result.status,
            "created_by": result.creater_id,
            "created_at": result.created_at,
            "last_updated_by": result.updater_id,
            "last_updated_at": result.updated_at,
        },
        "status": {
            "code": "I0001",
            "message": "",
            "detail": ""
        }
    }
    # "created_at" : result.created_at.strftime("%Y-%m-%d %H:%M:%S),
    # "updater_id" : result.updater_id,
    # "updated_at" : result.updated_at.strftime("%Y-%m-%d %H:%M:%S),
    return result_json


def getByIdWithLock(project_request):
    """
    /project3/lock/<id>で呼び出されたAPIの検索とロック処理

    Parameters
    ----------
    project_request: json
    {
       project_id : int,     検索するアカウントのアカウントID
       operation_account_id : int    Webアプリケーション操作アカウントのID
    }
    Returns
    -------
    ret
        json形式のアカウント詳細
    {
        "body": {
            "project_name": <project_name>,
            "description": <description>,
            "status": <status>,
            "created_by": <creater_id>,
            "created_at": <created_at>,
            "last_updated_by": <updater_id>,
            "last_updated_at": <update_at>
        },
        "status": {
            "code" : "I0001",
            "message" : "",
            "detail" : ""
        }
    }
    """
    body = ""
    project_id = project_request.get('id')
    operation_account_id = project_request.get('operation_account_id')

    try:
        result = Project.getByIdWithLock(project_id, operation_account_id)
        if result.id > 0:
            code = "I0001"
            message = "Locking project is successfully."
            body = {
                "id": result.id,
                "project_name": result.project_name,
                "description": result.description,
                "status":  result.status,
                "created_by": result.creater_id,
                "created_at": result.created_at,
                "last_updated_by": result.updater_id,
                "last_updated_at": result.updated_at,
            }
        else:
            code = "E0001"
            message = ""

    except:
        code = "E0009"
        message = "Locking project is fail."

    # TODO モデルの検索結果(正常・異常)によってレスポンスの出力内容を変える
    result_json = {
        "body": body,
        "status": {
            "code": "I0001",
            "message": "",
            "detail": ""
        }
    }
    return result_json


def create(project_request):
    """
    /project3/createで呼び出されたAPIの作成処理

    Parameters
    ----------
    project_request : json
        作成するアカウント詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    operation_account_id = project_request.get('operation_account_id')
    project = {
        'project_name': str(project_request['project_name']),
        'description': str(project_request['description']),
        'status': int(project_request['status']),
        'creater_id': operation_account_id,
        'created_at': datetime.datetime.now(),
        'updater_id': operation_account_id,
        'updated_at': datetime.datetime.now()
    }
    print(f"ProjectApi#create operation_account_id={operation_account_id}")
    try:
        if Project.create(project, operation_account_id) == True:
            code = "I0001"
            message = "Creating project was successfully."
        else:
            code = "E0001"
            message = ""

    except:
        code = "E0009"
        message = "Creating project was fail."

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json


def update(project_request):
    """
    /project3/updateで呼び出されたAPIの更新処理

    Parameters
    ----------
    project_request: json
    {
        "id": int, 変更するプロジェクトID
        "project_name": str
        "description": str
        "created_by": int
        "updated_by": int
        "status": int
        "operation_account_id": int, Webアプリケーション操作アカウントのID
    }

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    project = convertdict(project_request)
    operation_account_id = project_request.get('operation_account_id')
    try:
        res = Project.update(project, operation_account_id)
        print(f"ProjectApi#update res={res[0]},{res[1]}")
        if res[0] == True:
            code = "I0001"
            message = "Updating project was successfully."
        else:
            code = "E0001"
            message = res[1]

    except Exception as e:
        code = "E0009"
        print(f"update error={e}")
        message = f"Updating project was fail {e}"

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json


def updateWithLock(project_request):
    """
    /project3/update_for_lockで呼び出されたAPIの更新処理

    Parameters
    ----------
    project_request : json
        作成するプロジェクト詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    project = convertdict(project_request)
    if ('operation_account_id' in project_request):
        operation_account_id = int(project_request['operation_account_id'])
        try:
            res = Project.updateWithLock(project, operation_account_id)
            if res[0] == True:
                code = "I0001"
                message = "Updating project was successfully."
            else:
                code = "E0001"
                message = res[1]

        except Exception as e:
            code = "E0009"
            message = f"Updating project was fail {e}"
    else:
        code = "E0002"
        message = "Invalid Argument(operation_account_id is necessary)"

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json


def convertdict(from_dict):
    print(f"convertdict from_dict={from_dict}")
    target_dict = {}
    if ('id' in from_dict):
        target_dict['id'] = int(from_dict['id'])
    if ('project_name' in from_dict):
        target_dict['project_name'] = str(from_dict['project_name'])
    if ('description' in from_dict):
        target_dict['description'] = str(from_dict['description'])
    if ('status' in from_dict):
        target_dict['status'] = int(from_dict['status'])
    if ('creater_id' in from_dict):
        target_dict['creater_id'] = int(from_dict['creater_id'])
    if ('created_at' in from_dict):
        target_dict['created_at'] = strptime(from_dict['created_at'])
    if ('updater_id' in from_dict):
        target_dict['updater_id'] = int(from_dict['updater_id'])
    if ('updated_at' in from_dict):
        target_dict['updated_at'] = strptime(from_dict['updated_at'])
    if ('operation_account_id' in from_dict):
        target_dict['operation_account_id'] = int(
            from_dict['operation_account_id'])
    return target_dict
