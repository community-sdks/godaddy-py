from .abstract_service import AbstractService

class OrdersService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def list(self, x_app_key, period_start=None, period_end=None, domain=None, product_group_id=None, payment_profile_id=None, parent_order_id=None, offset=None, limit=None, sort=None, x_shopper_id=None, ):
        return self.call(
            "GET",
            "/v1/orders",
            [],
            [("periodStart", period_start), ("periodEnd", period_end), ("domain", domain), ("productGroupId", product_group_id), ("paymentProfileId", payment_profile_id), ("parentOrderId", parent_order_id), ("offset", offset), ("limit", limit), ("sort", sort)],
            [("X-Shopper-Id", x_shopper_id), ("X-App-Key", x_app_key)],
            None,
        )

    def get(self, order_id, x_app_key, x_shopper_id=None, x_market_id=None, ):
        return self.call(
            "GET",
            "/v1/orders/{orderId}",
            [("orderId", order_id)],
            [],
            [("X-Shopper-Id", x_shopper_id), ("X-Market-Id", x_market_id), ("X-App-Key", x_app_key)],
            None,
        )
