def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity in payload

    details = payload[expected_activity]
    assert set(["description", "schedule", "max_participants", "participants"]).issubset(details)
    assert isinstance(details["participants"], list)


def test_get_activities_includes_seed_participants(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    participants = payload["Programming Class"]["participants"]
    assert "emma@mergington.edu" in participants
    assert "sophia@mergington.edu" in participants
