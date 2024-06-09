import pytest
import os

from pages.email_page import EmailPage


def test_successful_email_sending(logged_in_test):
    home_page, token, user = logged_in_test
    email_page = home_page.click_email_on(user)
    email_page.verify_header("Edit user")
    sent_page = email_page.attempt_email("test subject", "test message", EmailPage)
    sent_page.get_alert().verify_alert_success("Email was scheduled to be send")
