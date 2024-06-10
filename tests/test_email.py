import pytest
import requests
import os

from pages.email_page import EmailPage


def test_successful_email_sending(logged_in_test):
    home_page, token, user = logged_in_test
    email_page = home_page.click_email_on(user)
    email_page.verify_header("Edit user")
    subject = "test subject"
    message = "test message"
    sent_page = email_page.attempt_email(subject, message, EmailPage)
    sent_page.get_alert().verify_alert_success("Email was scheduled to be send")

    response = requests.get(f"{os.getenv('MAILHOG_URL')}/api/v2/search?kind=to&query={user.email}&limit=1")
    data = response.json()
    assert data["items"][0]["Content"]["Headers"]["Subject"][0] == subject
    assert data["items"][0]["Content"]["Body"] == message


