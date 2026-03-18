import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    ("Pass@word1", True),
    ("Qwe@1uuuuuuuuuuuuuuu", False),
    ("Str@ng2", False),
])
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
