import uuid

import requests
from src.voicebox_wrapper import constants
from src.voicebox_wrapper.helpers import _success
from src.voicebox_wrapper.profile import Profile


class VoiceBox:
    def __init__(self, server_url: str = constants.DEFAULT_URL):
        """Creates a VoiceBox object.

        Args:
            server_url (str, optional): The URL for the VoiceBox API. Defaults to constants.DEFAULT_URL.
        """
        self._server_url = server_url
        self._profiles = []

    @property
    def profiles(self):
        """The list of Profile objects."""
        return self._profiles

    @property
    def server_url(self) -> str:
        """The root server URL of the VoiceBox API."""
        return self._server_url

    def _build_url(self, *parts) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"{self._server_url}/" + "/".join(parts)

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
        response = requests.post(
            self._build_url(constants.Endpoints.PROFILES), json=data
        )

        if not _success(response):
            raise Exception

        profile = Profile(self, response.json()["id"], name)
        self._profiles.append(profile)
        return profile

    def _delete_profile(self, profile: Profile):
        # todo - remove
        if profile in self._profiles:
            self._profiles.remove(profile)
        else:
            raise Exception
