# CountriesService

## Accessor

```python
service = client.countries()
```

## Method Index

- `get_countries`: `GetCountriesResponse`
- `get_country`: `GetCountryResponse`

### get_countries

Returns: `GetCountriesResponse`

```python
from godaddy.dto.countries.requests import GetCountriesRequest
request = GetCountriesRequest(
    market_id='abc123',
)
response = client.countries().get_countries(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_country

Returns: `GetCountryResponse`

```python
from godaddy.dto.countries.requests import GetCountryRequest
request = GetCountryRequest(
    country_key='value',
    market_id='abc123',
)
response = client.countries().get_country(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```