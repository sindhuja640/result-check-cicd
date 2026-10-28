
from app import app, get_result


def test_existing_student_passes():
    result = get_result("101")

    assert result is not None
    assert result["name"] == "Ananya"
    assert result["marks"] == 85
    assert result["status"] == "Pass"


def test_unknown_roll_number_returns_no_result():
    assert get_result("999") is None


def test_failing_student():
    result = get_result("103")

    assert result["status"] == "Fail"


def test_api_returns_404_for_unknown_student():
    client = app.test_client()
    response = client.get("/api/result/999")

    assert response.status_code == 404
