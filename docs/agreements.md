# AgreementsService

## Accessor

```python
service = client.agreements()
```

## Method Index

- `get`: `GetResponse`

### get

Returns: `GetResponse`

```python
from godaddy.dto.agreements.requests import GetRequest
request = GetRequest(
    x_private_label_id=1,
    x_market_id='abc123',
    keys=["value"],
)
response = client.agreements().get(request)
```

```json
[]
```