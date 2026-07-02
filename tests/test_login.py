from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("Admin", "admin123")
    login_page.wait_for_dashboard()
    assert "dashboard" in driver.current_url

def test_wrong_credential_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.wrong_credential_login("Sanjita", "Adhikari")
    assert "dashboard" not in driver.current_url

def test_invalid_username_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.invalid_username_login("User1@3$", "admin123")
    assert "dashboard" not in driver.current_url

def test_invalid_password_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.invalid_password_login("Admin", "password#@!2$")
    assert "dashboard" not in driver.current_url

def test_blank_username_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.blank_username_login("", "admin123")
    assert "dashboard" not in driver.current_url

def test_blank_password_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.blank_password_login("Admin", "")
    assert "dashboard" not in driver.current_url

def test_both_blank_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.both_blank_login("", "")
    assert "dashboard" not in driver.current_url

def test_both_fields_uppercase_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.both_fields_uppercase_login("ADMIN", "ADMIN123")
    assert "dashboard" not in driver.current_url

def test_maximum_length_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.maximum_characters_length_login("A" * 100, "P" * 100)
    assert "dashboard" not in driver.current_url
    