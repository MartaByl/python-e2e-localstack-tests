from typing import Type, TypeVar
from selenium import webdriver
from components.alert import AlertComponent
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

T = TypeVar('T', bound='AbstractBasePage')


class EmailPage(AbstractBasePage):
    header_h2 = (By.CSS_SELECTOR, "h2")
    subject_input = (By.NAME, "subject")
    message_input = (By.NAME, "message")
    send_email_button = (By.CSS_SELECTOR, "button.btn.btn-primary")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def attempt_email(self, subject: str, message: str, expected_page: Type[T]) -> T:
        self.driver.find_element(*self.subject_input).send_keys(subject)
        self.driver.find_element(*self.message_input).send_keys(message)
        self.driver.find_element(*self.send_email_button).click()
        return self.new_instance_of(expected_page)

    def get_alert(self):
        return AlertComponent(self.driver)

    def verify_header(self, expected_header: str):
        self.wait.until(EC.visibility_of_element_located(self.header_h2))
        actual_header = self.driver.find_element(*self.header_h2).text
        assert (
                expected_header in actual_header
        ), f"Expected header to be '{expected_header}' but found '{actual_header}'"
