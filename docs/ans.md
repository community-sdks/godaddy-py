# AnsService

## Accessor

```python
service = client.ans()
```

## Method Index

- `search_ansname`: `SearchAnsnameResponse`
- `register_agent`: `RegisterAgentResponse`
- `resolve_ansname`: `ResolveAnsnameResponse`
- `get_agent`: `GetAgentResponse`
- `revoke_agent`: `RevokeAgentResponse`
- `validate_registration`: `ValidateRegistrationResponse`
- `verify_dns_records`: `VerifyDnsRecordsResponse`
- `get_agent_identity_certificate_by_agent_id`: `GetAgentIdentityCertificateByAgentIdResponse`
- `submit_agent_identity_csr_by_agent_id`: `SubmitAgentIdentityCsrByAgentIdResponse`
- `get_agent_server_certificate_by_agent_id`: `GetAgentServerCertificateByAgentIdResponse`
- `submit_agent_server_csr_by_agent_id`: `SubmitAgentServerCsrByAgentIdResponse`
- `get_agent_csr_status_by_agent_id`: `GetAgentCsrStatusByAgentIdResponse`
- `get_agent_events`: `GetAgentEventsResponse`

### search_ansname

Returns: `SearchAnsnameResponse`

```python
from godaddy.dto.ans.requests import SearchAnsnameRequest
request = SearchAnsnameRequest(
    agent_display_name='value',
    version='value',
    agent_host='value',
    protocol='value',
)
response = client.ans().search_ansname(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### register_agent

Returns: `RegisterAgentResponse`

```python
from godaddy.dto.ans.requests import RegisterAgentRequest
request = RegisterAgentRequest(
    body={"key": "value"},
)
response = client.ans().register_agent(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### resolve_ansname

Returns: `ResolveAnsnameResponse`

```python
from godaddy.dto.ans.requests import ResolveAnsnameRequest
request = ResolveAnsnameRequest(
    body={"key": "value"},
)
response = client.ans().resolve_ansname(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_agent

Returns: `GetAgentResponse`

```python
from godaddy.dto.ans.requests import GetAgentRequest
request = GetAgentRequest(
    agent_id='abc123',
)
response = client.ans().get_agent(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### revoke_agent

Returns: `RevokeAgentResponse`

```python
from godaddy.dto.ans.requests import RevokeAgentRequest
request = RevokeAgentRequest(
    agent_id='abc123',
    body={"key": "value"},
)
response = client.ans().revoke_agent(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### validate_registration

Returns: `ValidateRegistrationResponse`

```python
from godaddy.dto.ans.requests import ValidateRegistrationRequest
request = ValidateRegistrationRequest(
    agent_id='abc123',
)
response = client.ans().validate_registration(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### verify_dns_records

Returns: `VerifyDnsRecordsResponse`

```python
from godaddy.dto.ans.requests import VerifyDnsRecordsRequest
request = VerifyDnsRecordsRequest(
    agent_id='abc123',
)
response = client.ans().verify_dns_records(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_agent_identity_certificate_by_agent_id

Returns: `GetAgentIdentityCertificateByAgentIdResponse`

```python
from godaddy.dto.ans.requests import GetAgentIdentityCertificateByAgentIdRequest
request = GetAgentIdentityCertificateByAgentIdRequest(
    agent_id='abc123',
)
response = client.ans().get_agent_identity_certificate_by_agent_id(request)
```

```json
[]
```

### submit_agent_identity_csr_by_agent_id

Returns: `SubmitAgentIdentityCsrByAgentIdResponse`

```python
from godaddy.dto.ans.requests import SubmitAgentIdentityCsrByAgentIdRequest
request = SubmitAgentIdentityCsrByAgentIdRequest(
    agent_id='abc123',
    body={"key": "value"},
)
response = client.ans().submit_agent_identity_csr_by_agent_id(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_agent_server_certificate_by_agent_id

Returns: `GetAgentServerCertificateByAgentIdResponse`

```python
from godaddy.dto.ans.requests import GetAgentServerCertificateByAgentIdRequest
request = GetAgentServerCertificateByAgentIdRequest(
    agent_id='abc123',
)
response = client.ans().get_agent_server_certificate_by_agent_id(request)
```

```json
[]
```

### submit_agent_server_csr_by_agent_id

Returns: `SubmitAgentServerCsrByAgentIdResponse`

```python
from godaddy.dto.ans.requests import SubmitAgentServerCsrByAgentIdRequest
request = SubmitAgentServerCsrByAgentIdRequest(
    agent_id='abc123',
    body={"key": "value"},
)
response = client.ans().submit_agent_server_csr_by_agent_id(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_agent_csr_status_by_agent_id

Returns: `GetAgentCsrStatusByAgentIdResponse`

```python
from godaddy.dto.ans.requests import GetAgentCsrStatusByAgentIdRequest
request = GetAgentCsrStatusByAgentIdRequest(
    agent_id='abc123',
    csr_id='abc123',
)
response = client.ans().get_agent_csr_status_by_agent_id(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_agent_events

Returns: `GetAgentEventsResponse`

```python
from godaddy.dto.ans.requests import GetAgentEventsRequest
request = GetAgentEventsRequest(
    x_request_id='abc123',
    provider_id='abc123',
    last_log_id='abc123',
    limit=1,
)
response = client.ans().get_agent_events(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```