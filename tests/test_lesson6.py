import pytest

@pytest.mark.parametrize("user_id,expected_status", [
    (1, 200),
    (2, 200),
    (1, 200),
    (9999, 404),
    (-1, 404),
])
def test_get_user_various_ids(api_context, user_id, expected_status):
    response = api_context.get(f"users/{user_id}")
    assert response.status == expected_status