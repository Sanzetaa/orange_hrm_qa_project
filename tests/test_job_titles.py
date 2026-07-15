from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.job_titles_page import JobTitlesPage


def test_job_titles_shows_records(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_job_titles_menu_item()

    job_titles = JobTitlesPage(driver)
    assert job_titles.page_is_displayed()
    job_titles.wait_for_loader_to_disappear()

    rows = job_titles.get_result_rows()
    assert len(rows) > 0