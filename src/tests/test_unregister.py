from urllib.parse import quote


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Programming Class"
    email = "emma@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{quote(activity_name, safe='')}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities_payload = client.get("/activities").json()
    assert email not in activities_payload[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange

    # Act
    response = client.delete("/activities/Unknown%20Club/participants", params={"email": "student@mergington.edu"})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_missing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-enrolled@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{quote(activity_name, safe='')}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not signed up for this activity"
