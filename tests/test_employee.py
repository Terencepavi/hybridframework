import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listner import WebDriverWrapper


class TestEmployee(WebDriverWrapper):
    @pytest.mark.parametrize("username, password, first_name, middle_name, last_name, full_name, verify_f_name", [
        ("Admin", "admin123", "John", "J", "wick", "John Wick", "John"),
        ("Admin", "admin123", "Peter", "J", "wick", "Peter Wick", "Peter")
    ])
    def test_valid_login(self, username, password, first_name, middle_name, last_name, full_name, verify_f_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.NAME, 'firstName').send_keys(first_name)
        self.driver.find_element(By.NAME, 'middleName').send_keys(middle_name)
        self.driver.find_element(By.NAME, 'lastName').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()
        time.sleep(5)

