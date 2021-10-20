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
