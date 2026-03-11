# ShoppersService

## Accessor

```python
service = client.shoppers()
```

## Method Index

- `create_subaccount`: `CreateSubaccountResponse`
- `get`: `GetResponse`
- `update`: `UpdateResponse`
- `delete`: `DeleteResponse`
- `get_status`: `GetStatusResponse`
- `change_password`: `ChangePasswordResponse`

### create_subaccount

Returns: `CreateSubaccountResponse`

```python
from godaddy.dto.shoppers.requests import CreateSubaccountRequest
request = CreateSubaccountRequest(
    subaccount='value',
)
response = client.shoppers().create_subaccount(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get

Returns: `GetResponse`

```python
from godaddy.dto.shoppers.requests import GetRequest
request = GetRequest(
    shopper_id='987654',
    includes=["value"],
)
response = client.shoppers().get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### update

Returns: `UpdateResponse`

```python
from godaddy.dto.shoppers.requests import UpdateRequest
request = UpdateRequest(
    shopper_id='987654',
    shopper='987654',
)
response = client.shoppers().update(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### delete

Returns: `DeleteResponse`

```python
from godaddy.dto.shoppers.requests import DeleteRequest
request = DeleteRequest(
    shopper_id='987654',
    audit_client_ip='value',
)
response = client.shoppers().delete(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_status

Returns: `GetStatusResponse`

```python
from godaddy.dto.shoppers.requests import GetStatusRequest
request = GetStatusRequest(
    shopper_id='987654',
    audit_client_ip='value',
)
response = client.shoppers().get_status(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### change_password

Returns: `ChangePasswordResponse`

```python
from godaddy.dto.shoppers.requests import ChangePasswordRequest
request = ChangePasswordRequest(
    shopper_id='987654',
    secret='value',
)
response = client.shoppers().change_password(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```