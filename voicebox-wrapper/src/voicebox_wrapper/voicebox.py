import uuid

import requests
import urllib3

PROFILES = "/profiles/"


class VoiceBox:
    def __init__(self, url: str = "http://127.0.0.1:17493"):
        self._url = url
        self._id = ""
        self._generation_id = None
        self._name = str(uuid.uuid4()).replace("-", "")[:6]

    def _success(self, response) -> int:
        return response.status_code == 200

    def create_profile(self) -> requests.Response:
        data = {"name": self._name}
        response = requests.post(self._url + PROFILES, json=data)

        if self._success(response):
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
        if not self._success(response):
            pass
        return response

    def begin_generating_audio(self, text: str) -> requests.Response:
        data = {"profile_id": self._id, "text": text}
        response = requests.post(self._url + "/generate", json=data)
        if self._success(response):
            self._generation_id = response.json()["id"]
        return response

    def _check_generation(self):
        return requests.get(f"{self._url}/history/{self._generation_id}")

    def generation_complete(self) -> bool:
        if self._generation_id is None:
            raise Exception
        else:
            response = self._check_generation()
            if self._success(response):
                return response.json()["status"] == "completed"

    def get_audio_path(self):
        response = self._check_generation()
        if self._success(response):
            return response.json()["audio_path"]

    def delete_profile(self) -> requests.Response:
        response = requests.delete(self._url + PROFILES + self._id)
        return response
