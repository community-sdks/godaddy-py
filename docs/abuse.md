# AbuseService

Abuse reporting and ticket lookup endpoints for phishing, malware, and related investigations.

## Accessor

```python
service = client.abuse()
```

## Endpoints

### get_tickets

Calls `GET /v1/abuse/tickets`.

```python
response = client.abuse().get_tickets('sample', True, 'sample', 'sample', 'sample', 'sample', 1, 1)
```

```json
{}
```

### create_ticket

Calls `POST /v1/abuse/tickets`.

```python
response = client.abuse().create_ticket({'sample': True})
```

```json
{}
```

### get_ticket_info

Calls `GET /v1/abuse/tickets/{ticketId}`.

```python
response = client.abuse().get_ticket_info('sample')
```

```json
{}
```

### get_tickets_v2

Calls `GET /v2/abuse/tickets`.

```python
response = client.abuse().get_tickets_v2('sample', True, 'sample', 'sample', 'sample', 'sample', 1, 1)
```

```json
{}
```

### create_ticket_v2

Calls `POST /v2/abuse/tickets`.

```python
response = client.abuse().create_ticket_v2({'sample': True})
```

```json
{}
```

### get_ticket_info_v2

Calls `GET /v2/abuse/tickets/{ticketId}`.

```python
response = client.abuse().get_ticket_info_v2('sample')
```

```json
{}
```

