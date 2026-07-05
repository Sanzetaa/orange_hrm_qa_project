from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

def test_open_admin_page(driver):

    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()

    admin = AdminPage(driver)

    assert admin.admin_page_is_displayed()