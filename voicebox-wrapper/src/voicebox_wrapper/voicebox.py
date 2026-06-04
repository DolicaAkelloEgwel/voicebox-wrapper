import uuid

import requests

from . import constants
from .helpers import _success
from .profile import Profile

PROFILES = "/profiles/"


class VoiceBox:
    def __init__(self, url: str = constants.DEFAULT_URL):
        self._url = url
        self._profiles = []

    def create_profile(self, name: str = str(uuid.uuid4())) -> Profile:
        data = {"name": name}
        response = requests.post(self._url + PROFILES, json=data)

        if _success(response):
            profile = Profile(self._url, response.json()["id"])
            self._profiles.append(profile)
            return profile
        else:
            raise Exception

    def delete_profile(self, profile_id: str):
        response = requests.delete(self._url + PROFILES + profile_id)
        if _success(response):
            pass
