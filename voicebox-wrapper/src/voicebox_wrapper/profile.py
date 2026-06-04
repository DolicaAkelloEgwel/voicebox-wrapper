from .helpers import _success
import urllib3


class Profile:

    def __init__(self, url: str, id: str):
        self._url = url
        self._id = id

    @property
    def id(self):
        return self._id

    def add_voice_sample(
        self, audio_data, filename: str, transcription: str
    ):
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