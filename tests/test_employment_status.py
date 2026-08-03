import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.employment_status_page import EmploymentStatusPage
from pages.add_employment_status_page import AddEmploymentStatusPage

def test_employment_status_shows_records(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_employee_status_menu_item()

    employment_status = EmploymentStatusPage(driver)
    assert employment_status.es_page_is_displayed()

    rows = employment_status.get_result_rows()

    assert len(rows)> 0

def test_add_employment_status(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")
    
    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()
    
    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()
    
    admin.click_job_dropdown()
    admin.click_employee_status_menu_item()
    
    employment_status = EmploymentStatusPage(driver)
    assert employment_status.es_page_is_displayed()

    employment_status.click_add_button()

    add_employment_status = AddEmploymentStatusPage(driver)
    assert add_employment_status.page_is_displayed()

    add_employment_status.type_name("Student")
    add_employment_status.click_save()

    assert employment_status.es_page_is_displayed()
    

    