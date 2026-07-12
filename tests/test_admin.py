from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
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

    admin.search_user("Admin")
    time.sleep(5)
    assert admin.get_first_result_username() == "Admin"

def test_random_username(driver):
    test_open_admin_page(driver)
    admin = AdminPage(driver)
    admin.search_user("Sanjita")
    time.sleep(5)
    assert admin.no_record_text_is_displayed()