from .abstract_service import AbstractService

class ShoppersService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def create_subaccount(self, subaccount, ):
        return self.call(
            "POST",
            "/v1/shoppers/subaccount",
            [],
            [],
            [],
            subaccount,
        )

    def get(self, shopper_id, includes=None, ):
        return self.call(
            "GET",
            "/v1/shoppers/{shopperId}",
            [("shopperId", shopper_id)],
            [("includes", includes)],
            [],
            None,
        )

    def update(self, shopper_id, shopper, ):
        return self.call(
            "POST",
            "/v1/shoppers/{shopperId}",
            [("shopperId", shopper_id)],
            [],
            [],
            shopper,
        )

    def delete(self, shopper_id, audit_client_ip, ):
        return self.call(
            "DELETE",
            "/v1/shoppers/{shopperId}",
            [("shopperId", shopper_id)],
            [("auditClientIp", audit_client_ip)],
            [],
            None,
        )

    def get_status(self, shopper_id, audit_client_ip, ):
        return self.call(
            "GET",
            "/v1/shoppers/{shopperId}/status",
            [("shopperId", shopper_id)],
            [("auditClientIp", audit_client_ip)],
            [],
            None,
        )

    def change_password(self, shopper_id, secret, ):
        return self.call(
            "PUT",
            "/v1/shoppers/{shopperId}/factors/password",
            [("shopperId", shopper_id)],
            [],
            [],
            secret,
        )
