# ParkingService

Domain parking optimization and template management endpoints.

## Accessor

```python
service = client.parking()
```

## Endpoints

### get_metrics

Calls `GET /v1/customers/{customerId}/parking/metrics`.

```python
response = client.parking().get_metrics('sample', 'sample', 'sample', 1, 1, 'header-value')
```

```json
{}
```

### get_metrics_by_domain

Calls `GET /v1/customers/{customerId}/parking/metricsByDomain`.

```python
response = client.parking().get_metrics_by_domain('sample', 'sample', 'sample', ['sample'], 'sample', 'sample', 1, 1, 'header-value')
```

```json
{}
```

