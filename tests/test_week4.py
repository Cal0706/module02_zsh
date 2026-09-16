# test_always_passes:


def test_always_passes():
    assert 2 + 2 == 4


# test_string_is_lowercase
def test_string_is_lowercase():
    name = "ism3232"
    assert name == name.lower()


# test_path_segments
def test_path_segments():
    path = "/Users/CamLopez/ism3232/module02_zsh"
    parts = path.split("/")
    assert "ism3232" in parts
