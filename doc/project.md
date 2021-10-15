# プロジェクト

## テーブル設計

### プロジェクトテーブル
|項目名|Field|Type|Null|Key|Default|Extra|Remark|
|---|---|---|---|---|---|---|---|
|プロジェクトID|project_id|varchar(30)|No|PRI|NULL|||
|プロジェクト名|project_name|varchar(60)|No||NULL|||
|説明|description|varchar(200)|Yes||NULL|||
|進行状況|status|int|No||0||0=未着手, 1=進行中, 2=完了|
|作成者ID|creater_id|varchar(20)|No||NULL|||
|作成日|created_at|datetime|No||NULL|||
|更新者ID|updater_id|varchar(20)|No||NULL|||
|更新日|updated_at|datetime|No||NULL|||
<br/>
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
        "created_at": <created_at>,
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

### プロジェクトの登録
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
    "created_at":
    "last_update_at":
}
```

#### response
```
{
    "body": {
        "project_id": <project_id>,
        "project_name": <project_name>,
        "description": <description>,
        "status": <status>,
        "created_at": <created_at>,
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