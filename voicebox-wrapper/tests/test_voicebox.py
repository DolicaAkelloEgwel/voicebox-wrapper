import requests
import src.voicebox_wrapper.constants as constants
from src.voicebox_wrapper.voicebox import VoiceBox


class MockResponse:
    status_code = None

    @staticmethod
    def json():
        return dict()


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
        response = MockResponse()
        response.status_code = 200
        response.json = lambda: {"id": profile_id}
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
        response = MockResponse()
        response.status_code = 200
        response.json = lambda: {"id": "a-profile-id"}
        return response

    monkeypatch.setattr(requests, "post", mock_post)

    vb = VoiceBox()
    profile = vb.create_profile()
    assert profile in vb.profiles


def test_create_profile_failure():
    pass


def test_delete_profile_success():
    pass


def test_delete_profile_failure():
    pass
