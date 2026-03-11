# GoDaddy Python SDK

Community-maintained Python SDK for the GoDaddy APIs. The SDK exposes one service accessor per API area and uses explicit request/response DTOs for every endpoint.

## Installation

```bash
pip install community-sdks-godaddy
```

## Configuration


```python
from godaddy import Client, Config

config = Config.sandbox(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
    timeout=30.0,
    max_retries=2,
)

# Production: Config.production(...)
# Service override: service_base_urls={"domains": "https://api.godaddy.com"}

client = Client(config)
```

## Quick Start

```python
from godaddy import Client, Config
from godaddy.dto.abuse.requests import GetTicketsRequest

client = Client(Config.sandbox(api_key="KEY", api_secret="SECRET"))
response = client.abuse().get_tickets(GetTicketsRequest(limit=20, offset=0))

print(response.raw)
```

## Services

- [Abuse](docs/abuse.md): `client.abuse()`
- [Aftermarket](docs/aftermarket.md): `client.aftermarket()`
- [Agreements](docs/agreements.md): `client.agreements()`
- [Ans](docs/ans.md): `client.ans()`
- [Auctions](docs/auctions.md): `client.auctions()`
- [Certificates](docs/certificates.md): `client.certificates()`
- [Countries](docs/countries.md): `client.countries()`
- [Domains](docs/domains.md): `client.domains()`
- [Orders](docs/orders.md): `client.orders()`
- [Parking](docs/parking.md): `client.parking()`
- [Shoppers](docs/shoppers.md): `client.shoppers()`
- [Subscriptions](docs/subscriptions.md): `client.subscriptions()`

See `docs/` for endpoint-by-endpoint request and response examples.
