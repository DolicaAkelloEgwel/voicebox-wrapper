import pytest
import src.voicebox_wrapper.constants as constants
from src.voicebox_wrapper.voicebox import VoiceBox, _success


@pytest.fixture
def mock_response():
    class MockResponse(object):
        status_code = None

    return MockResponse()


def test_set_url():
    url = "http://127.0.0.1:55555"
    vb = VoiceBox(url)
    assert vb._url == url


def test_default_url():
    vb = VoiceBox()
    assert vb._url == constants.DEFAULT_URL


def test_given_code_200_then_success_returns_true(mock_response):
    mock_response.status_code = 200
    assert _success(mock_response)
