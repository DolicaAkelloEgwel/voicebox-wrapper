import requests

def _success(response: requests.Response) -> bool:
    return response.status_code == 200