from godaddy.errors import ApiException


class AbstractService:
    def __init__(self, client, service_name):
        self._client = client
        self._service_name = service_name

    def _execute(self, method, path, path_params=None, query_params=None, headers=None, body=None):
        try:
            return self._client.request(
                method,
                self._service_name,
                path,
                path_params or [],
                query_params or [],
                headers or [],
                body,
            )
        except ApiException as exception:
            raise self._map_exception(exception) from exception

    def _map_exception(self, exception: ApiException) -> ApiException:
        return exception
