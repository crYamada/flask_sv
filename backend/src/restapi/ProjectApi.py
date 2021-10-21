from model import Project
from model import Status
#from __future__ import absolute_import, unicode_literals
import json
import datetime
from model.common import strftime
from model.common import strptime

#import requests


def delete(project_id, operation_account_id):
    """
    /project3/deleteで呼び出されたAPIの検索処理

    Parameters
    ----------
    project_id : int
        削除するプロジェクトID
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    try:
        res = Project.delete(project_id, operation_account_id)
        if res[0] == True:
            code = "I0001"
            message = "Deleting project was successfully."
        else:
            code = "E0001"
            message = res[1]

    except Exception as e:
        code = "E0009"
        message = f"Deleting project was fail:{str(e)}"

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json
