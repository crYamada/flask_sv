from model import Project
from model import Status
#from __future__ import absolute_import, unicode_literals
import json
import datetime
from model.common import strftime
from model.common import strptime

#import requests


def create(project_request):
    """
    /project/createで呼び出されたAPIの作成処理

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
            message = "Created project was successfully."
        else:
            code = "E0001"
            message = ""

    except:
        code = "E0009"
        message = "Created project was failed."

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json
