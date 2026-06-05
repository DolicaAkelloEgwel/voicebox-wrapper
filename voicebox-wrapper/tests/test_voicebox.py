from unittest.mock import patch

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


@patch("src.voicebox_wrapper.voicebox.requests")
def test_create_profile_sets_id(mock_requests):
    profile_id = "a-profile-id"
    mock_requests.post.return_value = MockResponse(200, {"id": profile_id})

    vb = VoiceBox()
    profile = vb.create_profile()

    assert profile.id == profile_id


@patch("src.voicebox_wrapper.voicebox.requests")
def test_create_profile_with_custom_name(mock_requests):
    custom_profile_name = "custom-profile-name"

    mock_requests.post.return_value = MockResponse(200, {"id": "profile-id"})

    vb = VoiceBox()
    profile = vb.create_profile(custom_profile_name)

    assert profile.name == custom_profile_name
    mock_requests.post.assert_called_with(
        vb._url + constants.PROFILES, json={"name": custom_profile_name}
    )


@patch("src.voicebox_wrapper.voicebox.requests")
@patch("src.voicebox_wrapper.voicebox.uuid")
def test_create_profile_with_default_name(mock_uuid, mock_requests):
    mock_requests.post.return_value = MockResponse(200, {"id": "profile-id"})
    mock_uuid.uuid4.return_value = default_name = "a-uuid-name"

    vb = VoiceBox()
    profile = vb.create_profile()

    assert profile.name == default_name
    mock_requests.post.assert_called_with(
        vb._url + constants.PROFILES, json={"name": default_name}
    )


@patch("src.voicebox_wrapper.voicebox.requests")
def test_create_profile_appends_list(mock_requests):
    mock_requests.post.return_value = MockResponse(200, {"id": "profile-id"})

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
