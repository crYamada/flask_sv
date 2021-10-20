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
    accountモデル
    flask_svシステムにログインするアカウントを管理するモデル

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
            'description':str(self.description),
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
            "status": int(self.status),
            "creater_id": int(self.creater_id),
            "created_at": strftime(self.created_at),
            "updater_id": int(self.updater_id),
            "updated_at": strftime(self.updated_at)
        }
