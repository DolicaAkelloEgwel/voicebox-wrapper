from src.voicebox_wrapper.voicebox import VoiceBox
import src.voicebox_wrapper.constants as constants
import pytest

def test_set_url():
    url = "http://127.0.0.1:55555"
    vb = VoiceBox(url)
    assert vb._url == url

def test_default_url():
    vb = VoiceBox()
    assert vb._url == constants.DEFAULT_URL