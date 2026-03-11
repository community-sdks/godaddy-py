class ApiException(Exception):
    def __init__(self, message, status_code, response_body=None, response_headers=None, method=None, url=None, error_response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        self.response_headers = response_headers or {}
        self.method = method
        self.url = url
        self.error_response = error_response


class ValidationException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class RateLimitException(ApiException):
    pass


class ServerException(ApiException):
    pass


class AbuseApiException(ApiException):
    pass

class AbuseBadRequestException(ValidationException):
    pass

class AbuseUnauthorizedException(UnauthorizedException):
    pass

class AbuseForbiddenException(UnauthorizedException):
    pass

class AbuseNotFoundException(NotFoundException):
    pass

class AbuseConflictException(ApiException):
    pass

class AbuseUnprocessableEntityException(ValidationException):
    pass

class AbuseRateLimitException(RateLimitException):
    pass

class AbuseServerException(ServerException):
    pass

class AftermarketApiException(ApiException):
    pass

class AftermarketBadRequestException(ValidationException):
    pass

class AftermarketUnauthorizedException(UnauthorizedException):
    pass

class AftermarketForbiddenException(UnauthorizedException):
    pass

class AftermarketNotFoundException(NotFoundException):
    pass

class AftermarketConflictException(ApiException):
    pass

class AftermarketUnprocessableEntityException(ValidationException):
    pass

class AftermarketRateLimitException(RateLimitException):
    pass

class AftermarketServerException(ServerException):
    pass

class AgreementsApiException(ApiException):
    pass

class AgreementsBadRequestException(ValidationException):
    pass

class AgreementsUnauthorizedException(UnauthorizedException):
    pass

class AgreementsForbiddenException(UnauthorizedException):
    pass

class AgreementsNotFoundException(NotFoundException):
    pass

class AgreementsConflictException(ApiException):
    pass

class AgreementsUnprocessableEntityException(ValidationException):
    pass

class AgreementsRateLimitException(RateLimitException):
    pass

class AgreementsServerException(ServerException):
    pass

class AnsApiException(ApiException):
    pass

class AnsBadRequestException(ValidationException):
    pass

class AnsUnauthorizedException(UnauthorizedException):
    pass

class AnsForbiddenException(UnauthorizedException):
    pass

class AnsNotFoundException(NotFoundException):
    pass

class AnsConflictException(ApiException):
    pass

class AnsUnprocessableEntityException(ValidationException):
    pass

class AnsRateLimitException(RateLimitException):
    pass

class AnsServerException(ServerException):
    pass

class AuctionsApiException(ApiException):
    pass

class AuctionsBadRequestException(ValidationException):
    pass

class AuctionsUnauthorizedException(UnauthorizedException):
    pass

class AuctionsForbiddenException(UnauthorizedException):
    pass

class AuctionsNotFoundException(NotFoundException):
    pass

class AuctionsConflictException(ApiException):
    pass

class AuctionsUnprocessableEntityException(ValidationException):
    pass

class AuctionsRateLimitException(RateLimitException):
    pass

class AuctionsServerException(ServerException):
    pass

class CertificatesApiException(ApiException):
    pass

class CertificatesBadRequestException(ValidationException):
    pass

class CertificatesUnauthorizedException(UnauthorizedException):
    pass

class CertificatesForbiddenException(UnauthorizedException):
    pass

class CertificatesNotFoundException(NotFoundException):
    pass

class CertificatesConflictException(ApiException):
    pass

class CertificatesUnprocessableEntityException(ValidationException):
    pass

class CertificatesRateLimitException(RateLimitException):
    pass

class CertificatesServerException(ServerException):
    pass

class CountriesApiException(ApiException):
    pass

class CountriesBadRequestException(ValidationException):
    pass

class CountriesUnauthorizedException(UnauthorizedException):
    pass

class CountriesForbiddenException(UnauthorizedException):
    pass

class CountriesNotFoundException(NotFoundException):
    pass

class CountriesConflictException(ApiException):
    pass

class CountriesUnprocessableEntityException(ValidationException):
    pass

class CountriesRateLimitException(RateLimitException):
    pass

class CountriesServerException(ServerException):
    pass

class DomainsApiException(ApiException):
    pass

class DomainsBadRequestException(ValidationException):
    pass

class DomainsUnauthorizedException(UnauthorizedException):
    pass

class DomainsForbiddenException(UnauthorizedException):
    pass

class DomainsNotFoundException(NotFoundException):
    pass

class DomainsConflictException(ApiException):
    pass

class DomainsUnprocessableEntityException(ValidationException):
    pass

class DomainsRateLimitException(RateLimitException):
    pass

class DomainsServerException(ServerException):
    pass

class OrdersApiException(ApiException):
    pass

class OrdersBadRequestException(ValidationException):
    pass

class OrdersUnauthorizedException(UnauthorizedException):
    pass

class OrdersForbiddenException(UnauthorizedException):
    pass

class OrdersNotFoundException(NotFoundException):
    pass

class OrdersConflictException(ApiException):
    pass

class OrdersUnprocessableEntityException(ValidationException):
    pass

class OrdersRateLimitException(RateLimitException):
    pass

class OrdersServerException(ServerException):
    pass

class ParkingApiException(ApiException):
    pass

class ParkingBadRequestException(ValidationException):
    pass

class ParkingUnauthorizedException(UnauthorizedException):
    pass

class ParkingForbiddenException(UnauthorizedException):
    pass

class ParkingNotFoundException(NotFoundException):
    pass

class ParkingConflictException(ApiException):
    pass

class ParkingUnprocessableEntityException(ValidationException):
    pass

class ParkingRateLimitException(RateLimitException):
    pass

class ParkingServerException(ServerException):
    pass

class ShoppersApiException(ApiException):
    pass

class ShoppersBadRequestException(ValidationException):
    pass

class ShoppersUnauthorizedException(UnauthorizedException):
    pass

class ShoppersForbiddenException(UnauthorizedException):
    pass

class ShoppersNotFoundException(NotFoundException):
    pass

class ShoppersConflictException(ApiException):
    pass

class ShoppersUnprocessableEntityException(ValidationException):
    pass

class ShoppersRateLimitException(RateLimitException):
    pass

class ShoppersServerException(ServerException):
    pass

class SubscriptionsApiException(ApiException):
    pass

class SubscriptionsBadRequestException(ValidationException):
    pass

class SubscriptionsUnauthorizedException(UnauthorizedException):
    pass

class SubscriptionsForbiddenException(UnauthorizedException):
    pass

class SubscriptionsNotFoundException(NotFoundException):
    pass

class SubscriptionsConflictException(ApiException):
    pass

class SubscriptionsUnprocessableEntityException(ValidationException):
    pass

class SubscriptionsRateLimitException(RateLimitException):
    pass

class SubscriptionsServerException(ServerException):
    pass