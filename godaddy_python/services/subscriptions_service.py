from .abstract_service import AbstractService

class SubscriptionsService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def list(self, x_app_key, x_shopper_id=None, x_market_id=None, product_group_keys=None, includes=None, offset=None, limit=None, sort=None, ):
        return self.call(
            "GET",
            "/v1/subscriptions",
            [],
            [("productGroupKeys", product_group_keys), ("includes", includes), ("offset", offset), ("limit", limit), ("sort", sort)],
            [("X-App-Key", x_app_key), ("X-Shopper-Id", x_shopper_id), ("X-Market-Id", x_market_id)],
            None,
        )

    def product_groups(self, x_app_key, x_shopper_id=None, ):
        return self.call(
            "GET",
            "/v1/subscriptions/productGroups",
            [],
            [],
            [("X-App-Key", x_app_key), ("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def cancel(self, subscription_id, x_app_key, x_shopper_id=None, ):
        return self.call(
            "DELETE",
            "/v1/subscriptions/{subscriptionId}",
            [("subscriptionId", subscription_id)],
            [],
            [("X-App-Key", x_app_key), ("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def get(self, subscription_id, x_app_key, x_shopper_id=None, ):
        return self.call(
            "GET",
            "/v1/subscriptions/{subscriptionId}",
            [("subscriptionId", subscription_id)],
            [],
            [("X-App-Key", x_app_key), ("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def update(self, subscription_id, x_app_key, subscription, x_shopper_id=None, ):
        return self.call(
            "PATCH",
            "/v1/subscriptions/{subscriptionId}",
            [("subscriptionId", subscription_id)],
            [],
            [("X-App-Key", x_app_key), ("X-Shopper-Id", x_shopper_id)],
            subscription,
        )
