class MockResponse:
    def __init__(self, code, json):
        self.status_code = code
        self.json = lambda: json


def test_delete_profile_failure():
    pass
    # mock_requests.delete.return_value = MockResponse(constants.REQUEST_SUCCESS, None)

    # profile_id_to_delete = "profile-id-to-delete"
    # profile = MockProfile(profile_id_to_delete)
    # vb = VoiceBox()
    # vb._profiles.append(profile)
    # assert profile in vb.profiles

    # vb._delete_profile(profile_id_to_delete)

    # assert profile not in vb.profiles
    # mock_requests.delete.assert_called_with(
    #     vb._url + constants.PROFILES + profile_id_to_delete
    # )


def test_delete_profile_success():
    pass
