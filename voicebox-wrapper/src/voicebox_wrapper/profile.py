import requests
import urllib3
from src.voicebox_wrapper.constants import PROFILES
from src.voicebox_wrapper.helpers import _success


class Profile:
    def __init__(self, voicebox, id: str, name: str):
        self._voicebox = voicebox
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def add_voice_sample(self, audio_data, filename: str, transcription: str):
        body, header = urllib3.encode_multipart_formdata(
            {
                "file": (filename, audio_data, "audio/wav"),
                "reference_text": transcription,
            }
        )
        response = requests.post(
            f"{self.voicebox.url}{PROFILES}{self._id}/samples",
            data=body,
            headers={"content-type": header},
        )
        if not _success(response):
            pass
        return response

    def begin_generating_audio(self, text: str):
        data = {"profile_id": self._id, "text": text}
        response = requests.post(self.voicebox.url + "/generate", json=data)
        if _success(response):
            self._generation_id = response.json()["id"]
        return response

    def _check_generation(self, generation_id: str):
        return requests.get(f"{self.voicebox.url}/history/{generation_id}")

    def generation_complete(self, generation_id: str) -> bool:
        response = self._check_generation(generation_id)
        if _success(response):
            return response.json()["status"] == "completed"

    def get_audio_path(self):
        response = self._check_generation()
        if _success(response):
            return response.json()["audio_path"]
