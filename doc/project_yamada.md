# プロジェクト

## テーブル設計
### プロジェクトテーブル
|項目名|Field|Type|Null|Key|Default|Extra|Remark|
|---|---|---|---|---|---|---|---|
|プロジェクトID|project_id|int|No|PRI|NULL|auto_increment||
|プロジェクト名|project_name|varchar(60)|No||NULL|||
|説明|description|varchar(200)|Yes||NULL|||
|進行状況|status|int|No||0||0=未着手, 1=進行中, 2=完了|
|作成者ID|creater_id|int|No||NULL|||
|作成日時|created_at|datetime|No||NULL|||
|更新者ID|updater_id|int|No||NULL|||
|更新日時|updated_at|datetime|No||NULL|||
<br>
***

## API設計

### project_idからの検索
#### URL
  /project/get/<project_id>
#### HTTP METHOD
  GET
#### request
  なし
#### response
```
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
```
***

### プロジェクトの新規登録
#### URL
  /project/add/
#### HTTP METHOD
  POST
#### request
```
{
    "project_id":
    "project_name":
    "description":
    "created_by":
    "updated_by":
    "staus":
}
```

#### response
```
{
    "body": "",
    "status": {
        "code" : "I0001",
        "message" : "project {} was added.",
        "detail" : ""
    }
}
```
***

### プロジェクトの修正・更新
#### URL
  /project/update/<project_id>
#### HTTP METHOD
  POST
#### request
```
{
    "project_name":
    "description":
    "created_by":
    "updated_by":
    "status":
}
```

#### response
```
{
    "body": "",
    "status": {
        "code" : "I0001",
        "message" : "project {} was updated.",
        "detail" : ""
    }
}
```
***

### プロジェクトの検索
#### URL
  /project/search/
#### HTTP METHOD
  POST
#### request
```
{
    "project_id":
    "project_name":
    "status":
    "created_by":
    "created_at":
    "updated_by":
    "last_update_at":
}
```

#### response
```
{
    "body": [
      {
          "project_id": <project_id>,
          "project_name": <project_name>,
          "description": <description>,
          "status": <status>,
          "created_by": <creater_id>,
          "created_at": <created_at>,
          "last_updated_by": <updater_id>,
          "last_updated_at": <update_at>
      },
      {
          "project_id": <project_id>,
          "project_name": <project_name>,
          "description": <description>,
          "status": <status>,
          "created_by": <creater_id>,
          "created_at": <created_at>,
          "last_updated_by": <updater_id>,
          "last_updated_at": <update_at>
      }
    ],
    "status": {
        "code" : "I0001",
        "message" : "",
        "detail" : ""
    }
}
```
***

### プロジェクトの削除
#### URL
  /project/delete/<project_id>
#### HTTP METHOD
  GET
#### request
  なし
#### response
```
{
    "body": "",
    "status": {
        "code" : "I0001",
        "message" : "project {} was deleted.",
        "detail" : ""
    }
}
```