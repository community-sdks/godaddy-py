from .abstract_service import AbstractService

class AgreementsService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def get(self, keys, x_private_label_id=None, x_market_id=None, ):
        return self.call(
            "GET",
            "/v1/agreements",
            [],
            [("keys", keys)],
            [("X-Private-Label-Id", x_private_label_id), ("X-Market-Id", x_market_id)],
            None,
        )
