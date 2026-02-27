# CountriesService

Country and market metadata endpoints used across purchase flows.

## Accessor

```python
service = client.countries()
```

## Endpoints

### get_countries

Calls `GET /v1/countries`.

```python
response = client.countries().get_countries('sample')
```

```json
{}
```

### get_country

Calls `GET /v1/countries/{countryKey}`.

```python
response = client.countries().get_country('sample', 'sample')
```

```json
{}
```

