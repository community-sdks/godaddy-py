# AuctionsService

Auction listing discovery endpoints for GoDaddy Auctions inventory.

## Accessor

```python
service = client.auctions()
```

## Endpoints

### place_bids

Calls `POST /v1/customers/{customerId}/aftermarket/listings/bids`.

```python
response = client.auctions().place_bids('sample', {'sample': True})
```

```json
{}
```

