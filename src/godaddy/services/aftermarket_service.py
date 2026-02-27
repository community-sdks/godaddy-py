from .abstract_service import AbstractService

class AftermarketService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def get_listings(self, customer_id, domains=None, listing_status=None, transfer_before=None, transfer_after=None, limit=None, offset=None, ):
        return self.call(
            "GET",
            "/v1/customers/{customerId}/auctions/listings",
            [("customerId", customer_id)],
            [("domains", domains), ("listingStatus", listing_status), ("transferBefore", transfer_before), ("transferAfter", transfer_after), ("limit", limit), ("offset", offset)],
            [],
            None,
        )

    def delete_listings(self, domains, ):
        return self.call(
            "DELETE",
            "/v1/aftermarket/listings",
            [],
            [("domains", domains)],
            [],
            None,
        )

    def add_expiry_listings(self, expiry_listings, ):
        return self.call(
            "POST",
            "/v1/aftermarket/listings/expiry",
            [],
            [],
            [],
            expiry_listings,
        )
