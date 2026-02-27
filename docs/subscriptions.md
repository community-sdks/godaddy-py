# SubscriptionsService

Subscription listing and management endpoints for recurring products.

## Accessor

```python
service = client.subscriptions()
```

## Endpoints

### list

Calls `GET /v1/subscriptions`.

```python
response = client.subscriptions().list('header-value', 'header-value', 'header-value', ['sample'], ['sample'], 1, 1, 'sample')
```

```json
{}
```

### product_groups

Calls `GET /v1/subscriptions/productGroups`.

```python
response = client.subscriptions().product_groups('header-value', 'header-value')
```

```json
{}
```

### cancel

Calls `DELETE /v1/subscriptions/{subscriptionId}`.

```python
response = client.subscriptions().cancel({'sample': True}, 'header-value', 'header-value')
```

```json
{}
```

### get

Calls `GET /v1/subscriptions/{subscriptionId}`.

```python
response = client.subscriptions().get({'sample': True}, 'header-value', 'header-value')
```

```json
{}
```

### update

Calls `PATCH /v1/subscriptions/{subscriptionId}`.

```python
response = client.subscriptions().update({'sample': True}, 'header-value', {'sample': True}, 'header-value')
```

```json
{}
```

