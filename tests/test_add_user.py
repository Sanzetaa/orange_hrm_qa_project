import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage

def test_add_new_user(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")
    
    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_add_button()
    add_user = AddUserPage(driver)
    assert add_user.add_user_page_is_displayed()


    add_user.select_user_role("ESS")
    add_user.type_employee_name("Sanjita Adhikari")   
    add_user.select_status("Enabled")
    add_user.type_username("testuser")
    add_user.type_password("Test@1234")
    add_user.click_save()

    time.sleep(3)
    admin2 = AdminPage(driver)
    assert admin2.admin_page_is_displayed()