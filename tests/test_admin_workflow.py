import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import OrangeHRMLoginPage
from pages.orangehrm_admin_page import OrangeHRMAdminPage 


def test_user_management(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    admin_page = OrangeHRMAdminPage(page)
   
    login_page.navigate()
    login_page.login("Admin", "admin123")
    admin_page.add_employee("Kg", "E", "Uh", "9909")
    admin_page.add_employee_as_user_by_admin()
    admin_page.confirm_added_user()
    admin_page.update_employee_personal_details()
    admin_page.update_employee_contact_details()
    admin_page.delete_employee_from_list() 