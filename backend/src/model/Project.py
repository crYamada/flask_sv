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
    # datetime.strptime(str(self.project_name), "%Y-%m-%d %H:%M:%S")

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


def update(project_dict, operation_account_id):
    project_id = project_dict.get('id')
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    res = False
    ses = Session()
    project_record = ses.query(Project).with_for_update().get(project_id)
    message = ""
    try:
        v = project_dict.get('project_name')
        if (v != None):
            project_record.project_name = v
        v = project_dict.get('description')
        if (v != None):
            project_record.description = v
        v = project_dict.get('status')
        if (v != None):
            project_record.status = v
        v = project_dict.get('creater_id')
        if (v != None):
            project_record.creater_id = v
        project_record.updater_id = operation_account_id
        project_record.updated_at = strftime(datetime.datetime.now())
        ses.add(project_record)
        # 他のプロセスによるロックを待つ
        # time.sleep(1)
        ses.commit()
        res = True

    except Exception as e:
        message = str(e)
        print(f"Project#update error:{message}")
        ses.rollback()
        res = False

    finally:
        ses.close()

    return (res, message)


def updateWithLock(project_dict, operation_account_id):
    project_id = project_dict.get('id')
    # session_poolよりセッション情報と検索結果を取得する
    (ses, project_record) = session_pool[operation_account_id]
    res = False
    print(f"Project#update project_record={project_record}")
    message = ""
    try:
        v = project_dict.get('project_name')
        if (v != None):
            project_record.project_name = v
        v = project_dict.get('description')
        if (v != None):
            project_record.description = v
        v = project_dict.get('status')
        if (v != None):
            project_record.status = v
        v = project_dict.get('creater_id')
        if (v != None):
            project_record.creater_id = v
        project_record.updater_id = operation_account_id
        project_record.updated_at = strftime(datetime.datetime.now())
        ses.add(project_record)
        # 他のプロセスによるロックを待つ
        # time.sleep(1)
        ses.commit()
        res = True

    except Exception as e:
        message = str(e)
        print(f"Project#updateWithLock error:{message}")
        ses.rollback()
        res = False

    finally:
        ses.close()

    return (res, message)


def search(project_dict, operation_account_id):
    """
    dictプロジェクトからprojectテーブルを検索し、該当したProjectオブジェクト群を取得する

    Parameters
    ----------
    {
        'id':
        'project_name':
        'status':
        'creater_id':
        'created_at':
        'updater_id':
        'updated_at':
    }

    Returns
    -------
    Projectオブジェクトのリスト
    """
    print(f"project_dict={project_dict}")
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = None
    rs = ses.query(Project)
    v = project_dict.get('id')
    if (v != None):
        rs = rs.filter(Project.id == v)
    v = project_dict.get('project_name')
    if (v != None):
        rs = rs.filter(Project.project_name == v)
    v = project_dict.get('status')
    if (v != None):
        rs = rs.filter(Project.status == v)
    v = project_dict.get('creater_id')
    if (v != None):
        rs = rs.filter(Project.creater_id == v)
    v = project_dict.get('created_at')
    if (v != None):
        rs = rs.filter(Project.created_at == v)
    v = project_dict.get('updater_id')
    if (v != None):
        rs = rs.filter(Project.updater_id == v)
    v = project_dict.get('updated_at')
    if (v != None):
        rs = rs.filter(Project.updated_at == v)

    res = rs.all()
    lambda r: print(f"r={r}"), res
    ses.close()
    return res


def delete(project_id, operation_account_id):
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    ses = Session()
    project_record = ses.query(Project).with_for_update().get(project_id)
    try:
        project_record.status = Status.getStatusKey("DELETE")
        ses.add(project_record)
        # 他のプロセスによるロックを待つ
        # time.sleep(1)
        ses.commit()
        message = ""
        res = True

    except Exception as e:
        message = str(e)
        print(f"Project#delete error:{message}")
        ses.rollback()
        res = False

    finally:
        ses.close()

    return (res, message)
