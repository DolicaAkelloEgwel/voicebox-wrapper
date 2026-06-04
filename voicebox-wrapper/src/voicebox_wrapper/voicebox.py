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

    def create_profile(self, name: str = str(uuid.uuid4())):
        data = {"name": name}
        response = requests.post(self._url + PROFILES, json=data)

        if _success(response):
            profile = Profile(self._url, response.json()["id"])
            self._profiles.append(profile)
            return profile
        else:
            raise Exception

    def begin_generating_audio(self, text: str):
        data = {"profile_id": self._id, "text": text}
        response = requests.post(self._url + "/generate", json=data)
        if _success(response):
            self._generation_id = response.json()["id"]
        return response

    def _check_generation(self, generation_id: str):
        return requests.get(f"{self._url}/history/{generation_id}")

    def generation_complete(self, generation_id: str) -> bool:
        response = self._check_generation(generation_id)
        if _success(response):
            return response.json()["status"] == "completed"

    def get_audio_path(self):
        response = self._check_generation()
        if _success(response):
            return response.json()["audio_path"]

    def delete_profile(self, profile_id: str):
        response = requests.delete(self._url + PROFILES + profile_id)
        return response
