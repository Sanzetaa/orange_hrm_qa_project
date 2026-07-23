from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.pay_grades_page import PayGradesPage
from pages.add_pay_grade_page import AddPayGradePage

def test_pay_grades_shows_rows(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_pay_grades_menu_item()

    pay_grades = PayGradesPage(driver)
    assert pay_grades.page_is_displayed()

    rows = pay_grades.get_result_rows()
    assert len(rows) > 0

def test_add_button_redirects_to_add_pay_grade_page(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_pay_grades_menu_item()

    pay_grades = PayGradesPage(driver)
    assert pay_grades.page_is_displayed()

    pay_grades.click_add_button()

    add_pay_grade = AddPayGradePage(driver)
    assert add_pay_grade.page_is_displayed()