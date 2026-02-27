# AnsService

Authoritative DNS record and nameserver management endpoints.

## Accessor

```python
service = client.ans()
```

## Endpoints

### search_ans_name

Calls `GET /v1/agents`.

```python
response = client.ans().search_ans_name('sample', 'sample', 'sample', 'sample', 1, 1)
```

```json
{}
```

### register_agent

Calls `POST /v1/agents/register`.

```python
response = client.ans().register_agent({'sample': True})
```

```json
{}
```

### resolve_ans_name

Calls `POST /v1/agents/resolution`.

```python
response = client.ans().resolve_ans_name({'sample': True})
```

```json
{}
```

### get_agent

Calls `GET /v1/agents/{agentId}`.

```python
response = client.ans().get_agent('sample')
```

```json
{}
```

### validate_registration

Calls `POST /v1/agents/{agentId}/verify-acme`.

```python
response = client.ans().validate_registration('sample')
```

```json
{}
```

### verify_dns_records

Calls `POST /v1/agents/{agentId}/verify-dns`.

```python
response = client.ans().verify_dns_records('sample')
```

```json
{}
```

### get_agent_identity_certificate_by_agent_id

Calls `GET /v1/agents/{agentId}/certificates/identity`.

```python
response = client.ans().get_agent_identity_certificate_by_agent_id('sample')
```

```json
{}
```

### submit_agent_identity_csr_by_agent_id

Calls `POST /v1/agents/{agentId}/certificates/identity`.

```python
response = client.ans().submit_agent_identity_csr_by_agent_id('sample', {'sample': True})
```

```json
{}
```

### get_agent_server_certificate_by_agent_id

Calls `GET /v1/agents/{agentId}/certificates/server`.

```python
response = client.ans().get_agent_server_certificate_by_agent_id('sample')
```

```json
{}
```

### submit_agent_server_csr_by_agent_id

Calls `POST /v1/agents/{agentId}/certificates/server`.

```python
response = client.ans().submit_agent_server_csr_by_agent_id('sample', {'sample': True})
```

```json
{}
```

### get_agent_csr_status_by_agent_id

Calls `GET /v1/agents/{agentId}/csrs/{csrId}/status`.

```python
response = client.ans().get_agent_csr_status_by_agent_id('sample', 'sample')
```

```json
{}
```

### get_agent_events

Calls `GET /v1/agents/events`.

```python
response = client.ans().get_agent_events('header-value', 'sample', 'sample', 1)
```

```json
{}
```

