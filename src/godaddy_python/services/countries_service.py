from .abstract_service import AbstractService

class CountriesService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def get_countries(self, market_id, ):
        return self.call(
            "GET",
            "/v1/countries",
            [],
            [("marketId", market_id)],
            [],
            None,
        )

    def get_country(self, country_key, market_id, ):
        return self.call(
            "GET",
            "/v1/countries/{countryKey}",
            [("countryKey", country_key)],
            [("marketId", market_id)],
            [],
            None,
        )
