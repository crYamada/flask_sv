from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
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
