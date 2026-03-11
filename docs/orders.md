# OrdersService

## Accessor

```python
service = client.orders()
```

## Method Index

- `list`: `ListResponse`
- `get`: `GetResponse`

### list

Returns: `ListResponse`

```python
from godaddy.dto.orders.requests import ListRequest
request = ListRequest(
    period_start='value',
    period_end='value',
    domain='example.com',
    product_group_id=1,
)
response = client.orders().list(request)
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
from godaddy.dto.orders.requests import GetRequest
request = GetRequest(
    order_id='abc123',
    x_shopper_id='987654',
    x_market_id='abc123',
    x_app_key='value',
)
response = client.orders().get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```