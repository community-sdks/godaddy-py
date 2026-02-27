# ShoppersService

Shopper profile, account, and delegated access endpoints.

## Accessor

```python
service = client.shoppers()
```

## Endpoints

### create_subaccount

Calls `POST /v1/shoppers/subaccount`.

```python
response = client.shoppers().create_subaccount({'sample': True})
```

```json
{}
```

### get

Calls `GET /v1/shoppers/{shopperId}`.

```python
response = client.shoppers().get({'sample': True}, ['sample'])
```

```json
{}
```

### update

Calls `POST /v1/shoppers/{shopperId}`.

```python
response = client.shoppers().update({'sample': True}, {'sample': True})
```

```json
{}
```

### delete

Calls `DELETE /v1/shoppers/{shopperId}`.

```python
response = client.shoppers().delete({'sample': True}, 'sample')
```

```json
{}
```

### get_status

Calls `GET /v1/shoppers/{shopperId}/status`.

```python
response = client.shoppers().get_status({'sample': True}, 'sample')
```

```json
{}
```

### change_password

Calls `PUT /v1/shoppers/{shopperId}/factors/password`.

```python
response = client.shoppers().change_password({'sample': True}, {'sample': True})
```

```json
{}
```

