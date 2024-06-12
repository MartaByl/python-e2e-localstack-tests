import pytest
import requests

from api.data.register import User
from generators.user_generator import generate_username, generate_password
from api.post_sign_up import SignUp


def test_signup_with_too_short_firstname():
    # Generate a username with a short first name (1 character)
    username = generate_username()
    password = generate_password()
    email = "test@example.com"
    roles = ["ROLE_ADMIN"]
    firstName = "A"  # intentionally short first name
    lastName = "Doe"

    # Create the request body
    user = User(
        username=username,
        email=email,
        password=password,
        roles=roles,
        firstName=firstName,
        lastName=lastName
    )

    try:
        # Send the signup request
        SignUp().api_call(user)

    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 400, "Expected status code 400"
        assert "Minimum firstName length: 4 characters" == e.response.json()[
            "firstName"], "Expected error message for wrong first name"

def test_signup_with_too_short_lastname():
    # Generate a username and password
    username = generate_username()
    password = generate_password()
    email = "test@example.com"
    roles = ["ROLE_ADMIN"]
    firstName = "John"
    lastName = "D"  # intentionally short last name

    # Create the request body
    user = User(
        username=username,
        email=email,
        password=password,
        roles=roles,
        firstName=firstName,
        lastName=lastName
    )

    try:
        # Send the signup request
        SignUp().api_call(user)

    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 400, "Expected status code 400"
        assert "Minimum lastName length: 4 characters" == e.response.json()[
            "lastName"], "Expected error message for wrong last name"
