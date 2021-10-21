from model import Project
from model import Status
#from __future__ import absolute_import, unicode_literals
import json
import datetime
from model.common import strftime
from model.common import strptime

#import requests


def search(request):
    """
    /project3/searchで呼び出されたAPIの検索処理

    Parameters
    ----------
    project_request : json
        アカウント検索項目
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    operation_account_id = request.get('operation_account_id')
    project_request = convertdict(request)
    try:
        results = Project.search(project_request, operation_account_id)
        code = "I0001"
        message = f"Found ({len(results)}) records."
        body = list(map(lambda s: s.toJson(), results))

    except Exception as e:
        code = "E0009"
        message = "Search failed: " + str(e)
        body = ""

    result_json = {
        "body": body,
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
