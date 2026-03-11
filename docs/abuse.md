# AbuseService

## Accessor

```python
service = client.abuse()
```

## Method Index

- `get_tickets`: `GetTicketsResponse`
- `create_ticket`: `CreateTicketResponse`
- `get_ticket_info`: `GetTicketInfoResponse`
- `get_tickets_v2`: `GetTicketsV2Response`
- `create_ticket_v2`: `CreateTicketV2Response`
- `get_ticket_info_v2`: `GetTicketInfoV2Response`

### get_tickets

Returns: `GetTicketsResponse`

```python
from godaddy.dto.abuse.requests import GetTicketsRequest
request = GetTicketsRequest(
    type_value='value',
    closed=True,
    source_domain_or_ip='example.com',
    target='value',
)
response = client.abuse().get_tickets(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### create_ticket

Returns: `CreateTicketResponse`

```python
from godaddy.dto.abuse.requests import CreateTicketRequest
request = CreateTicketRequest(
    body={"key": "value"},
)
response = client.abuse().create_ticket(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_ticket_info

Returns: `GetTicketInfoResponse`

```python
from godaddy.dto.abuse.requests import GetTicketInfoRequest
request = GetTicketInfoRequest(
    ticket_id='TCK-100001',
)
response = client.abuse().get_ticket_info(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_tickets_v2

Returns: `GetTicketsV2Response`

```python
from godaddy.dto.abuse.requests import GetTicketsV2Request
request = GetTicketsV2Request(
    type_value='value',
    closed=True,
    source_domain_or_ip='example.com',
    target='value',
)
response = client.abuse().get_tickets_v2(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### create_ticket_v2

Returns: `CreateTicketV2Response`

```python
from godaddy.dto.abuse.requests import CreateTicketV2Request
request = CreateTicketV2Request(
    body={"key": "value"},
)
response = client.abuse().create_ticket_v2(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_ticket_info_v2

Returns: `GetTicketInfoV2Response`

```python
from godaddy.dto.abuse.requests import GetTicketInfoV2Request
request = GetTicketInfoV2Request(
    ticket_id='TCK-100001',
)
response = client.abuse().get_ticket_info_v2(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```