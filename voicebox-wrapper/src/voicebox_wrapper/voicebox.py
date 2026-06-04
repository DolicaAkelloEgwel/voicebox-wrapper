import uuid

import requests
import urllib3

from . import constants

PROFILES = "/profiles/"


def _success(response: requests.Response) -> bool:
    return response.status_code == 200


class VoiceBox:
    def __init__(self, url: str = constants.DEFAULT_URL):
        self._url = url

    def create_profile(self, name: str = str(uuid.uuid4())) -> requests.Response:
        data = {"name": name}
        response = requests.post(self._url + PROFILES, json=data)

        if _success(response):
            self._id = response.json()["id"]
        else:
            # this means creating a profile failed
            pass
        return response

    def add_voice_sample(
        self, audio_data, filename: str, transcription: str
    ) -> requests.Response:
        body, header = urllib3.encode_multipart_formdata(
            {
                "file": (filename, audio_data, "audio/wav"),
                "reference_text": transcription,
            }
        )
        response = requests.post(
            f"{self._url}{PROFILES}{self._id}/samples",
            data=body,
            headers={"content-type": header},
        )
        if not _success(response):
            pass
        return response

    def begin_generating_audio(self, text: str) -> requests.Response:
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

    def delete_profile(self, profile_id: str) -> requests.Response:
        response = requests.delete(self._url + PROFILES + profile_id)
        return response
