from godaddy.errors import ApiException
from godaddy.errors import ShoppersApiException, ShoppersBadRequestException, ShoppersConflictException, ShoppersForbiddenException, ShoppersNotFoundException, ShoppersRateLimitException, ShoppersServerException, ShoppersUnauthorizedException, ShoppersUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.shoppers.requests import CreateSubaccountRequest, GetRequest, UpdateRequest, DeleteRequest, GetStatusRequest, ChangePasswordRequest
from godaddy.dto.shoppers.responses import CreateSubaccountResponse, GetResponse, UpdateResponse, DeleteResponse, GetStatusResponse, ChangePasswordResponse

class ShoppersService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "shoppers")

    def create_subaccount(self, request: CreateSubaccountRequest | None = None) -> CreateSubaccountResponse:
        request = request or CreateSubaccountRequest()
        response = self._execute(
            "POST",
            "/v1/shoppers/subaccount",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CreateSubaccountResponse.from_mixed(response)

    def get(self, request: GetRequest | None = None) -> GetResponse:
        request = request or GetRequest()
        response = self._execute(
            "GET",
            "/v1/shoppers/{shopperId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetResponse.from_mixed(response)

    def update(self, request: UpdateRequest | None = None) -> UpdateResponse:
        request = request or UpdateRequest()
        response = self._execute(
            "POST",
            "/v1/shoppers/{shopperId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return UpdateResponse.from_mixed(response)

    def delete(self, request: DeleteRequest | None = None) -> DeleteResponse:
        request = request or DeleteRequest()
        response = self._execute(
            "DELETE",
            "/v1/shoppers/{shopperId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DeleteResponse.from_mixed(response)

    def get_status(self, request: GetStatusRequest | None = None) -> GetStatusResponse:
        request = request or GetStatusRequest()
        response = self._execute(
            "GET",
            "/v1/shoppers/{shopperId}/status",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetStatusResponse.from_mixed(response)

    def change_password(self, request: ChangePasswordRequest | None = None) -> ChangePasswordResponse:
        request = request or ChangePasswordRequest()
        response = self._execute(
            "PUT",
            "/v1/shoppers/{shopperId}/factors/password",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ChangePasswordResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return ShoppersBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return ShoppersUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return ShoppersForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return ShoppersNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return ShoppersConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return ShoppersUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return ShoppersRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return ShoppersServerException(*exception.args, error_response=exception.error_response)
        return ShoppersApiException(*exception.args, error_response=exception.error_response)