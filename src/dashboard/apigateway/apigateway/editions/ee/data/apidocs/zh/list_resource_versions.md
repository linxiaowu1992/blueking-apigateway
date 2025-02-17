### 描述

查询资源版本

### 输入参数

#### 路径参数

| 参数名称 | 参数类型 | 必选 | 描述   |
| -------- | -------- | ---- | ------ |
| api_name | string   | 是   | 网关名 |

#### 请求参数

| 参数名称 | 参数类型 | 必选 | 描述   |
| -------- | -------- | ---- | ------ |
| version  | string   | 否   | 版本号 |

### 请求参数示例

```json
{
    "version": "1.0.0"
}
```

### SDK 调用示例

```python
from bkapi.bk_apigateway.shortcuts import get_client_by_request

client = get_client_by_request(request)
result = client.api.list_resource_versions({"version": "1.0.0"})
```


### 响应示例

```json
{
    "data": {
        "count": 1,
        "has_next": false,
        "has_previous": false,
        "results": [
            {
                "version": "1.0.0",
                "title": "test",
                "comment": ""
            }
        ]
    },
    "code": 0,
    "result": true,
    "message": "OK"
}
```

### 响应参数说明

| 字段    | 类型   | 描述                               |
| ------- | ------ | ---------------------------------- |
| code    | int    | 返回码，0 表示成功，其它值表示失败 |
| message | string | 错误信息                           |
| data    | array  | 结果数据，详细信息请见下面说明     |

#### data.results

| 参数名称 | 参数类型 | 描述     |
| -------- | -------- | -------- |
| version  | string   | 版本号   |
| title    | string   | 版本标题 |
| comment  | string   | 版本说明 |
