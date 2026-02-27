# AftermarketService

Aftermarket listing and sales endpoints for secondary-market domain workflows.

## Accessor

```python
service = client.aftermarket()
```

## Endpoints

### get_listings

Calls `GET /v1/customers/{customerId}/auctions/listings`.

```python
response = client.aftermarket().get_listings('sample', ['sample'], ['sample'], 'sample', 'sample', 1, 1)
```

```json
{}
```

### delete_listings

Calls `DELETE /v1/aftermarket/listings`.

```python
response = client.aftermarket().delete_listings(['sample'])
```

```json
{}
```

### add_expiry_listings

Calls `POST /v1/aftermarket/listings/expiry`.

```python
response = client.aftermarket().add_expiry_listings(['sample'])
```

```json
{}
```

