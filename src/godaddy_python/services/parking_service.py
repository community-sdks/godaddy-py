from .abstract_service import AbstractService

class ParkingService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def get_metrics(self, customer_id, period_start_ptz=None, period_end_ptz=None, limit=None, offset=None, x_request_id=None, ):
        return self.call(
            "GET",
            "/v1/customers/{customerId}/parking/metrics",
            [("customerId", customer_id)],
            [("periodStartPtz", period_start_ptz), ("periodEndPtz", period_end_ptz), ("limit", limit), ("offset", offset)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_metrics_by_domain(self, customer_id, start_date, end_date, domains=None, domain_like=None, portfolio_id=None, limit=None, offset=None, x_request_id=None, ):
        return self.call(
            "GET",
            "/v1/customers/{customerId}/parking/metricsByDomain",
            [("customerId", customer_id)],
            [("startDate", start_date), ("endDate", end_date), ("domains", domains), ("domainLike", domain_like), ("portfolioId", portfolio_id), ("limit", limit), ("offset", offset)],
            [("X-Request-Id", x_request_id)],
            None,
        )
