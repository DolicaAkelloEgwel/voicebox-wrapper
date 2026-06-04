import pytest
from src.voicebox_wrapper.helpers import _success


@pytest.fixture
def mock_response():
    class MockResponse(object):
        status_code = None

    return MockResponse()


def test_given_code_200_then_success_returns_true(mock_response):
    mock_response.status_code = 200
    assert _success(mock_response)


def test_given_code_not_200_then_success_returns_false(mock_response):
    mock_response.status_code = 300
    assert not _success(mock_response)
