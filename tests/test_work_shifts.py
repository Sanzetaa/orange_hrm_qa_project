import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.work_shifts_page import WorkShiftsPage

def test_work_shifts_shows_records(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_work_shifts_menu_item()

    work_shifts = WorkShiftsPage(driver)
    assert work_shifts.page_is_displayed()

    rows = work_shifts.get_result_rows()
    assert len(rows) > 0

def test_add_work_shift(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_work_shifts_menu_item()

    work_shifts = WorkShiftsPage(driver)
    assert work_shifts.page_is_displayed()

    work_shifts.click_add_button()
    assert work_shifts.add_page_is_displayed()

    
    work_shifts.type_name("SampleShift")
    work_shifts.click_save()

    assert work_shifts.get_success_message() == "Successfully Saved"
    
    