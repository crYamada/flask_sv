from model import db
from model import Project
from model import Status
import pprint
import datetime


def test_getById():
    """
    """

    project = {
        'project_name': 'flask_sv',
        'description': 'test of getById',
        'status': 0,
        'creater_id': 999,
        'created_at': '2021-01-01 00:00:00',
        'updater_id': 999,
        'updated_at': '2021-12-31 00:00:00'
    }

    Project.create(project, 999) == True

    project_dict = {
        'project_name': "flask_sv",
        'status': 0
    }
    results = Project.search(project_dict, 1)
    project_id = results[0].id
    result = Project.getById(project_id, 999)

    assert result.project_name == project['project_name']
    assert result.description == project['description']
    assert result.status == project['status']
    assert result.creater_id == project['creater_id']
    assert result.created_at == datetime.datetime.strptime(
        project['created_at'], '%Y-%m-%d %H:%M:%S')
    assert result.updater_id == project['updater_id']
    assert result.updated_at == datetime.datetime.strptime(
        project['updated_at'], '%Y-%m-%d %H:%M:%S')

    assert results[0].project_name == project['project_name']
    assert results[0].description == project['description']
    assert results[0].status == project['status']
    assert results[0].creater_id == project['creater_id']
    assert results[0].created_at == datetime.datetime.strptime(
        project['created_at'], '%Y-%m-%d %H:%M:%S')
    assert results[0].updater_id == project['updater_id']
    assert results[0].updated_at == datetime.datetime.strptime(
        project['updated_at'], '%Y-%m-%d %H:%M:%S')
