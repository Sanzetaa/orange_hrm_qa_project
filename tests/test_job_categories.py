import time 
from conftest import driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.job_categories_page import JobCategoriesPage
from pages.add_job_category_page import AddJobCategoryPage

def test_job_categories_shows_records(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_job_categories_menu_item()

    job_categories = JobCategoriesPage(driver)
    assert job_categories.page_is_displayed()

    rows = job_categories.get_result_rows()
    assert len(rows) > 0

def test_add_job_category(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    assert dashboard.dashboard_is_visible()
    dashboard.click_admin_menu()

    admin = AdminPage(driver)
    assert admin.admin_page_is_displayed()

    admin.click_job_dropdown()
    admin.click_job_categories_menu_item()

    job_categories = JobCategoriesPage(driver)
    assert job_categories.page_is_displayed()   

    job_categories.click_add_button()

    add_job_category = AddJobCategoryPage(driver)
    assert add_job_category.page_is_displayed()

    add_job_category.type_name("testingg")
    add_job_category.click_save()

    assert add_job_category.get_success_message() == "Successfully Saved"
