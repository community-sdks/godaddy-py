from .abstract_service import AbstractService

class AuctionsService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def place_bids(self, customer_id, request_body, ):
        return self.call(
            "POST",
            "/v1/customers/{customerId}/aftermarket/listings/bids",
            [("customerId", customer_id)],
            [],
            [],
            request_body,
        )
