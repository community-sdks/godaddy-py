from .api_client import ApiClient
from .config import Config
from .services import AbuseService, AftermarketService, AgreementsService, AnsService, AuctionsService, CertificatesService, CountriesService, DomainsService, OrdersService, ParkingService, ShoppersService, SubscriptionsService

class Client:
    def __init__(self, config=None, transport=None):
        self._api_client = ApiClient(config or Config(), transport)
        self._abuse = AbuseService(self._api_client)
        self._aftermarket = AftermarketService(self._api_client)
        self._agreements = AgreementsService(self._api_client)
        self._ans = AnsService(self._api_client)
        self._auctions = AuctionsService(self._api_client)
        self._certificates = CertificatesService(self._api_client)
        self._countries = CountriesService(self._api_client)
        self._domains = DomainsService(self._api_client)
        self._orders = OrdersService(self._api_client)
        self._parking = ParkingService(self._api_client)
        self._shoppers = ShoppersService(self._api_client)
        self._subscriptions = SubscriptionsService(self._api_client)

    def api_client(self):
        return self._api_client

    def abuse(self):
        return self._abuse

    def aftermarket(self):
        return self._aftermarket

    def agreements(self):
        return self._agreements

    def ans(self):
        return self._ans

    def auctions(self):
        return self._auctions

    def certificates(self):
        return self._certificates

    def countries(self):
        return self._countries

    def domains(self):
        return self._domains

    def orders(self):
        return self._orders

    def parking(self):
        return self._parking

    def shoppers(self):
        return self._shoppers

    def subscriptions(self):
        return self._subscriptions
