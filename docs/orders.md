# OrdersService

Order lookup endpoints for commerce and fulfillment status.

## Accessor

```python
service = client.orders()
```

## Endpoints

### list

Calls `GET /v1/orders`.

```python
response = client.orders().list('header-value', 'sample', 'sample', 'sample', 'sample', 'sample', 'sample', 1, 1, 'sample', 'header-value')
```

```json
{}
```

### get

Calls `GET /v1/orders/{orderId}`.

```python
response = client.orders().get('sample', 'header-value', 'header-value', 'header-value')
```

```json
{}
```

