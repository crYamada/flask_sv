from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.expression import column
from model import Status
import sqlalchemy
from model.common import strftime
from model.common import strptime
import time
import model.Status
from session import session_pool
# from sqlalch

import datetime
#from datetime import datetime

from model.db import engine
from model.db import Base

# model class


class Project(Base):
    """
    projectモデル
    案件などのプロジェクトを管理するモデル

    Parameters
    ----------
    Base : データベース接続子
    """
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    project_name = Column(String())
    description = Column(String(), nullable=True)
    status = Column(Integer)
    creater_id = Column(Integer)
    created_at = Column(Timestamp)
    updater_id = Column(Integer)
    updated_at = Column(Timestamp)

    # get Dict data
    def toDict(self):
        """
        ディクショナリ形式でクラスの全メンバを返却する

        Parameters
        ----------
        self : 自クラス

        Returns
        -------
        クラスの全メンバのディクショナリ
        """
        return {
            'id': int(self.id),
            'project_name': str(self.project_name),
            'description': str(self.description),
            'status': int(self.status),
            'creater_id': int(self.creater_id),
            'created_at': strptime(self.created_at),
            'updater_id': int(self.updater_id),
            'updated_at': strptime(self.updated_at)
        }
    # datetime.strptime(str(self.start_on), "%Y-%m-%d %H:%M:%S")

    def toJson(self):
        return {
            "id": str(self.id),
            "project_name": self.project_name,
            "description": self.description,
            "status": int(self.status),
            "creater_id": int(self.creater_id),
            "created_at": strftime(self.created_at),
            "updater_id": int(self.updater_id),
            "updated_at": strftime(self.updated_at)
        }

# get List data


def getByList(arr):
    res = []
    for item in arr:
        res.append(item.toDict())
    return res

# get all mydata record


def getAll():
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(Project).all()
    ses.close()
    return res


def getById(project_id, operation_account_id):
    """
    アカウントidでaccountテーブルを検索をし、該当したAccountオブジェクト群を取得する

    Parameters
    ----------
    project_id : 検索対象のアカウントid
    operation_account_id : 操作ユーザーのアカウントid

    Returns
    -------
    Accountオブジェクトのリスト
    """
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(Project).get(project_id)
    ses.close()
    return res


def getByIdWithLock(project_id, operation_account_id):
    """
    アカウントidでaccountテーブルを検索をし、該当したAccountオブジェクト群を取得する

    Parameters
    ----------
    project_id: 検索対象のアカウントid
    operation_account_id : 操作ユーザーのアカウントid

    Returns
    -------
    Accountオブジェクトのリスト
    """
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    ses = Session()
    res = ses.query(Project).get(project_id)
    session_pool[operation_account_id] = (ses, res)
    # ses.close()


def create(project_dict, operation_account_id):
    project = Project()
    project.project_name = project_dict['project_name']
    project.description = project_dict['description']
    project.status = project_dict['status']
    project.creater_id = project_dict['creater_id']
    project.created_at = project_dict['created_at']
    project.updater_id = project_dict['updater_id']
    project.updated_at = project_dict['updated_at']
    Session = sessionmaker(bind=engine)
    ses = Session()
    ses.begin()
    try:
        ses.add(project)
        ses.commit()
        res = True

    except:
        ses.rollback()
        res = False

    finally:
        ses.close()

    return res
