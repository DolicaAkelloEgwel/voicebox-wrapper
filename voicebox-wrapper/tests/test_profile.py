from src.voicebox_wrapper.profile import Profile


class MockResponse:
    def __init__(self, code, json):
        self.status_code = code
        self.json = lambda: json


class MockVoicebox:
    def __init__(self):
        pass


def test_profile_stores_id_on_init():
    vb = MockVoicebox()
    id = "a-profile-id"
    name = "a-profile-name"
    profile = Profile(vb, id, name)

    assert profile.id == id
    assert profile.name == name
    assert profile._voicebox == vb


def test_add_voice_sample_success():
    pass


def test_add_voice_sample_failure():
    pass


def test_delete_profile_success():
    pass


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
