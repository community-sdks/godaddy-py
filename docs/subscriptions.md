# SubscriptionsService

## Accessor

```python
service = client.subscriptions()
```

## Method Index

- `list`: `ListResponse`
- `product_groups`: `ProductGroupsResponse`
- `get`: `GetResponse`
- `update`: `UpdateResponse`
- `cancel`: `CancelResponse`

### list

Returns: `ListResponse`

```python
from godaddy.dto.subscriptions.requests import ListRequest
request = ListRequest(
    x_app_key='value',
    x_shopper_id='987654',
    x_market_id='abc123',
    product_group_keys=["value"],
)
response = client.subscriptions().list(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### product_groups

Returns: `ProductGroupsResponse`

```python
from godaddy.dto.subscriptions.requests import ProductGroupsRequest
request = ProductGroupsRequest(
    x_app_key='value',
    x_shopper_id='987654',
)
response = client.subscriptions().product_groups(request)
```

```json
[]
```

### get

Returns: `GetResponse`

```python
from godaddy.dto.subscriptions.requests import GetRequest
request = GetRequest(
    x_app_key='value',
    x_shopper_id='987654',
    subscription_id='abc123',
)
response = client.subscriptions().get(request)
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
from godaddy.dto.subscriptions.requests import UpdateRequest
request = UpdateRequest(
    x_app_key='value',
    x_shopper_id='987654',
    subscription_id='abc123',
    subscription='value',
)
response = client.subscriptions().update(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### cancel

Returns: `CancelResponse`

```python
from godaddy.dto.subscriptions.requests import CancelRequest
request = CancelRequest(
    x_app_key='value',
    x_shopper_id='987654',
    subscription_id='abc123',
)
response = client.subscriptions().cancel(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```