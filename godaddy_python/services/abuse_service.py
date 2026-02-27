from .abstract_service import AbstractService

class AbuseService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def get_tickets(self, type=None, closed=None, source_domain_or_ip=None, target=None, created_start=None, created_end=None, limit=None, offset=None, ):
        return self.call(
            "GET",
            "/v1/abuse/tickets",
            [],
            [("type", type), ("closed", closed), ("sourceDomainOrIp", source_domain_or_ip), ("target", target), ("createdStart", created_start), ("createdEnd", created_end), ("limit", limit), ("offset", offset)],
            [],
            None,
        )

    def create_ticket(self, body, ):
        return self.call(
            "POST",
            "/v1/abuse/tickets",
            [],
            [],
            [],
            body,
        )

    def get_ticket_info(self, ticket_id, ):
        return self.call(
            "GET",
            "/v1/abuse/tickets/{ticketId}",
            [("ticketId", ticket_id)],
            [],
            [],
            None,
        )

    def get_tickets_v2(self, type=None, closed=None, source_domain_or_ip=None, target=None, created_start=None, created_end=None, limit=None, offset=None, ):
        return self.call(
            "GET",
            "/v2/abuse/tickets",
            [],
            [("type", type), ("closed", closed), ("sourceDomainOrIp", source_domain_or_ip), ("target", target), ("createdStart", created_start), ("createdEnd", created_end), ("limit", limit), ("offset", offset)],
            [],
            None,
        )

    def create_ticket_v2(self, body, ):
        return self.call(
            "POST",
            "/v2/abuse/tickets",
            [],
            [],
            [],
            body,
        )

    def get_ticket_info_v2(self, ticket_id, ):
        return self.call(
            "GET",
            "/v2/abuse/tickets/{ticketId}",
            [("ticketId", ticket_id)],
            [],
            [],
            None,
        )
