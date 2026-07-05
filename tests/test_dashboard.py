from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_is_visible(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.dashboard_is_visible()