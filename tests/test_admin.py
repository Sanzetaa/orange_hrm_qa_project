from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
import time

def test_open_admin_page(driver):

    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()

    admin = AdminPage(driver)

    assert admin.admin_page_is_displayed()

def test_search_user_by_username(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()
    
    admin = AdminPage(driver)

    assert admin.admin_page_is_displayed()

    admin.search_username("Admin")
    time.sleep(5)
    assert admin.get_first_result_username() == "Admin"

def test_invalid_username(driver):
    test_open_admin_page(driver)
    admin = AdminPage(driver)
    admin.search_username("Sanjita")
    time.sleep(5)
    assert admin.no_record_text_is_displayed()

def test_reset_button_clears_all_fields(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.search_username("Admin")
    admin.select_user_role("Admin")
    admin.select_status("Enabled")

    admin.click_reset()

    assert admin.get_username_field_value() == ""

def test_add_button(driver):
    test_open_admin_page(driver)
    admin = AdminPage(driver)
    admin.click_add_button()
    assert admin.add_user_page_is_displayed()

def test_orangeHRM_link(driver):
    test_open_admin_page(driver)
    admin = AdminPage(driver)
    original_window = driver.current_window_handle
    admin.click_orangeHRM_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "orangehrm.com" in driver.current_url
    driver.close()
    driver.switch_to.window(original_window)
