from .abstract_service import AbstractService

class AnsService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def search_ans_name(self, agent_display_name=None, version=None, agent_host=None, protocol=None, limit=None, offset=None, ):
        return self.call(
            "GET",
            "/v1/agents",
            [],
            [("agentDisplayName", agent_display_name), ("version", version), ("agentHost", agent_host), ("protocol", protocol), ("limit", limit), ("offset", offset)],
            [],
            None,
        )

    def register_agent(self, body, ):
        return self.call(
            "POST",
            "/v1/agents/register",
            [],
            [],
            [],
            body,
        )

    def resolve_ans_name(self, body, ):
        return self.call(
            "POST",
            "/v1/agents/resolution",
            [],
            [],
            [],
            body,
        )

    def get_agent(self, agent_id, ):
        return self.call(
            "GET",
            "/v1/agents/{agentId}",
            [("agentId", agent_id)],
            [],
            [],
            None,
        )

    def validate_registration(self, agent_id, ):
        return self.call(
            "POST",
            "/v1/agents/{agentId}/verify-acme",
            [("agentId", agent_id)],
            [],
            [],
            None,
        )

    def verify_dns_records(self, agent_id, ):
        return self.call(
            "POST",
            "/v1/agents/{agentId}/verify-dns",
            [("agentId", agent_id)],
            [],
            [],
            None,
        )

    def get_agent_identity_certificate_by_agent_id(self, agent_id, ):
        return self.call(
            "GET",
            "/v1/agents/{agentId}/certificates/identity",
            [("agentId", agent_id)],
            [],
            [],
            None,
        )

    def submit_agent_identity_csr_by_agent_id(self, agent_id, body, ):
        return self.call(
            "POST",
            "/v1/agents/{agentId}/certificates/identity",
            [("agentId", agent_id)],
            [],
            [],
            body,
        )

    def get_agent_server_certificate_by_agent_id(self, agent_id, ):
        return self.call(
            "GET",
            "/v1/agents/{agentId}/certificates/server",
            [("agentId", agent_id)],
            [],
            [],
            None,
        )

    def submit_agent_server_csr_by_agent_id(self, agent_id, body, ):
        return self.call(
            "POST",
            "/v1/agents/{agentId}/certificates/server",
            [("agentId", agent_id)],
            [],
            [],
            body,
        )

    def get_agent_csr_status_by_agent_id(self, agent_id, csr_id, ):
        return self.call(
            "GET",
            "/v1/agents/{agentId}/csrs/{csrId}/status",
            [("agentId", agent_id), ("csrId", csr_id)],
            [],
            [],
            None,
        )

    def get_agent_events(self, x_request_id=None, provider_id=None, last_log_id=None, limit=None, ):
        return self.call(
            "GET",
            "/v1/agents/events",
            [],
            [("providerId", provider_id), ("lastLogId", last_log_id), ("limit", limit)],
            [("X-Request-Id", x_request_id)],
            None,
        )
