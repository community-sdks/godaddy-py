# AftermarketService

## Accessor

```python
service = client.aftermarket()
```

## Method Index

- `get_listings`: `GetListingsResponse`
- `delete_listings`: `DeleteListingsResponse`
- `add_expiry_listings`: `AddExpiryListingsResponse`

### get_listings

Returns: `GetListingsResponse`

```python
from godaddy.dto.aftermarket.requests import GetListingsRequest
request = GetListingsRequest(
    customer_id='123456',
    domains='example.com',
    listing_status='ACTIVE',
    transfer_before='value',
)
response = client.aftermarket().get_listings(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### delete_listings

Returns: `DeleteListingsResponse`

```python
from godaddy.dto.aftermarket.requests import DeleteListingsRequest
request = DeleteListingsRequest(
    domains=["example.com"],
)
response = client.aftermarket().delete_listings(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### add_expiry_listings

Returns: `AddExpiryListingsResponse`

```python
from godaddy.dto.aftermarket.requests import AddExpiryListingsRequest
request = AddExpiryListingsRequest(
    expiry_listings=["value"],
)
response = client.aftermarket().add_expiry_listings(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```