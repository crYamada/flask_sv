# API

## account検索（時間の範囲指定可能）

#### URL

/account/search_range

#### HTTP METHOD

POST

#### request

```
{
	"account_name":"flask_sv2", 
	"from_start_on":"2021-05-01 00:00:00", 	
	"to_start_on":"2021-05-31 00:00:00", 	
  "from_end_on":"2030-12-01 00:00:00",
  "to_end_on":"2030-12-31 00:00:00",
}
```


#### response

```
{
	"body": "",
   "status": {
   		"code" : code,
   		"message" : message,
       "detail" : ""
   }
}
```

