import re
from playwright.sync_api import Page
from pages.orangehrm_login_page import OrangeHRMLoginPage
from pages.orangehrm_dashboardpage import OrangeHRMDashboardPage

def test_valid_login(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    dashboard_page = OrangeHRMDashboardPage(page)
    
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    dashboard_page.is_dashboard_visible()

def test_invalid_login_1(page: Page) -> None:
    login_page= OrangeHRMLoginPage(page)
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("wrongpasswordAdmin3")
    login_page.click_login()
    login_page.get_error_message()

def test_invalid_login_2(page: Page) -> None:
    login_page= OrangeHRMLoginPage(page)
    login_page.navigate()
    login_page.enter_username("WrongUsernameAdm")
    login_page.enter_password("admin123")
    login_page.click_login()
    login_page.get_error_message()
    
def test_login_with_empty_fields_1(page: Page) -> None:
    login_page= OrangeHRMLoginPage(page)
    login_page.navigate()
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    login_page.get_empty_field_error_message()
    
def test_login_with_empty_fields_2(page: Page) -> None:
    login_page= OrangeHRMLoginPage(page)
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("")
    login_page.click_login()
    login_page.get_empty_field_error_message()
    
def test_login_with_empty_fields_3(page: Page) -> None:
    login_page= OrangeHRMLoginPage(page)
    login_page.navigate()
    login_page.enter_username("")
    login_page.enter_password("admin123")
    login_page.click_login()
    login_page.get_empty_field_error_message()

def test_logout(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    dashboard_page = OrangeHRMDashboardPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")
    dashboard_page.is_dashboard_visible()
    dashboard_page.profile_picture_click()
    dashboard_page.click_logout()