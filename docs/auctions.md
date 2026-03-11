# AuctionsService

## Accessor

```python
service = client.auctions()
```

## Method Index

- `place_bids`: `PlaceBidsResponse`

### place_bids

Returns: `PlaceBidsResponse`

```python
from godaddy.dto.auctions.requests import PlaceBidsRequest
request = PlaceBidsRequest(
    customer_id='123456',
    request_body=["value"],
)
response = client.auctions().place_bids(request)
```

```json
[]
```