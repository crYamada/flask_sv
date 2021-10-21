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
