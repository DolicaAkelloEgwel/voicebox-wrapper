import uuid

import requests
from src.voicebox_wrapper import constants
from src.voicebox_wrapper.helpers import _success
from src.voicebox_wrapper.profile import Profile


class VoiceBox:
    def __init__(self, url: str = constants.DEFAULT_URL):
        """Creates a VoiceBox object.

        Args:
            url (str, optional): The URL for the VoiceBox API. Defaults to constants.DEFAULT_URL.
        """
        self._url = url
        self._profiles = []

    @property
    def profiles(self):
        return self._profiles

    @property
    def url(self) -> str:
        return self._url

    def create_profile(self, name: str = "") -> Profile:
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to str(uuid.uuid4()).

        Raises:
            Exception: _description_

        Returns:
            Profile: _description_
        """
        if not name:
            name = str(uuid.uuid4())

        data = {"name": name}
        response = requests.post(self._url + constants.PROFILES, json=data)

        if not _success(response):
            raise Exception

        profile = Profile(self, response.json()["id"], name)
        self._profiles.append(profile)
        return profile

    def _delete_profile(self, profile_id: str):
        response = requests.delete(self._url + constants.PROFILES + profile_id)
        if not _success(response):
            raise Exception

        for profile in self._profiles:
            if profile.id == profile_id:
                self._profiles.remove(profile)
                return
