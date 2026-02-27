class AbstractService:
    def __init__(self, client, base_url):
        self._client = client
        self._base_url = base_url

    def call(self, method, path, path_params=None, query_params=None, headers=None, body=None):
        return self._client.request(method, self._base_url, path, path_params or [], query_params or [], headers or [], body)
