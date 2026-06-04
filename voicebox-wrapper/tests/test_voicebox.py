import requests
import src.voicebox_wrapper.constants as constants
from src.voicebox_wrapper.voicebox import VoiceBox


class MockResponse:
    def __init__(self, code, json):
        self.status_code = code
        self.json = lambda: json


def test_set_url():
    url = "http://127.0.0.1:55555"
    vb = VoiceBox(url)
    assert vb._url == url


def test_default_url():
    vb = VoiceBox()
    assert vb._url == constants.DEFAULT_URL


def test_create_profile_sets_id(monkeypatch):

    profile_id = "a-profile-id"

    def mock_post(*args, **kwargs):
        response = MockResponse(200, {"id": profile_id})
        return response

    monkeypatch.setattr(requests, "post", mock_post)

    vb = VoiceBox()
    profile = vb.create_profile("a-profile-name")

    assert profile.id == profile_id


def test_create_profile_with_custom_name():
    pass


def test_create_profile_with_default_name():
    pass


def test_create_profile_appends_list(monkeypatch):
    def mock_post(*args, **kwargs):
        response = MockResponse(200, {"id": "a-profile-id"})
        return response

    monkeypatch.setattr(requests, "post", mock_post)

    vb = VoiceBox()
    assert len(vb.profiles) == 0
    profile = vb.create_profile()
    assert profile in vb.profiles


def test_create_profile_failure():
    pass


def test_delete_profile_success():
    pass


def test_delete_profile_failure():
    pass
