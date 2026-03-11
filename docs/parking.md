# ParkingService

## Accessor

```python
service = client.parking()
```

## Method Index

- `get_metrics`: `GetMetricsResponse`
- `get_metrics_by_domain`: `GetMetricsByDomainResponse`

### get_metrics

Returns: `GetMetricsResponse`

```python
from godaddy.dto.parking.requests import GetMetricsRequest
request = GetMetricsRequest(
    customer_id='123456',
    period_start_ptz='value',
    period_end_ptz='value',
    limit=1,
)
response = client.parking().get_metrics(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_metrics_by_domain

Returns: `GetMetricsByDomainResponse`

```python
from godaddy.dto.parking.requests import GetMetricsByDomainRequest
request = GetMetricsByDomainRequest(
    customer_id='123456',
    start_date='2024-01-01T00:00:00Z',
    end_date='2024-01-01T00:00:00Z',
    domains='example.com',
)
response = client.parking().get_metrics_by_domain(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```