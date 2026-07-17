import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.job_titles_page import JobTitlesPage
from pages.add_job_title_page import AddJobTitlePage

def test_add_job_title(driver):
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

    job_titles.click_add_button()

    add_job_title = AddJobTitlePage(driver)
    assert add_job_title.page_is_displayed()

    add_job_title.type_job_title("Automation Tester")
    add_job_title.type_job_description("Created by automated test")
    add_job_title.attach_job_specification(r"C:\Users\Hp\Downloads\QA_Job.pdf")
    add_job_title.type_note("This is a test note added via automation.")
    add_job_title.click_save()

    assert add_job_title.get_success_message() == "Successfully Saved"