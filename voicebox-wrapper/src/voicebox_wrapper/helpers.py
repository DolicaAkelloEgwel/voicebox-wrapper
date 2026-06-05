import requests
from src.voicebox_wrapper.constants import REQUEST_SUCCESS


def _success(response: requests.Response) -> bool:
    return response.status_code == REQUEST_SUCCESS
