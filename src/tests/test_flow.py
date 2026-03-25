from urllib.parse import quote


def test_signup_then_unregister_updates_state_transitions(client):
    # Arrange
    activity_name = "Art Studio"
    email = "flow-student@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    signup_response = client.post(f"/activities/{activity_path}/signup", params={"email": email})
    after_signup = client.get("/activities").json()[activity_name]["participants"]

    unregister_response = client.delete(
        f"/activities/{activity_path}/participants",
        params={"email": email},
    )
    after_unregister = client.get("/activities").json()[activity_name]["participants"]

    # Assert
    assert signup_response.status_code == 200
    assert email in after_signup

    assert unregister_response.status_code == 200
    assert email not in after_unregister
