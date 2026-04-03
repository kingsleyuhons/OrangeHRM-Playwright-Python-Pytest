from playwright.sync_api import Page, expect    

class OrangeHRMAdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_link = page.get_by_role("link", name="PIM")
        self.add_employee_button = page.get_by_role("button", name=" Add")
        self.first_name_input = page.get_by_role("textbox", name="First Name")  
        self.middle_name_input = page.get_by_role("textbox", name="Middle Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name") 
        self.employee_Id_input = page.locator("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.save_button = page.get_by_role("button", name="Save")
        self.assert_employee = page.locator("#app")
        self.admin_link = page.get_by_role("link", name="Admin")
        self.add_user_button = page.get_by_role("button", name=" Add")
        self.employee_name_input = page.get_by_role("textbox", name="Type for hints...")    
        self.employee_name_option = page.get_by_role("option", name="Kg E Uh")
        self.user_role_dropdown = page.get_by_text("-- Select --").first
        self.user_role_option = page.get_by_role("option", name="ESS")
        self.status_dropdown = page.get_by_text("-- Select --")
        self.status_option = page.get_by_role("option", name="Enabled")
        self.username_input = page.get_by_role("textbox").nth(2)    
        self.password_input = page.get_by_role("textbox").nth(3)
        self.confirm_password_input = page.get_by_role("textbox").nth(4)
        self.save_user_button = page.get_by_role("button", name="Save")
        self.assert_added_user = page.get_by_role("table")
        self.search_added_user_name_input = page.get_by_role("textbox", name="Type for hints...")
        self.search_name = page.get_by_role ("textbox", name="Type for hints...")
        self.search_name_option = page.get_by_text("Kg E Uh")
        self.search_button = page.get_by_role("button", name="Search")
        self.assert_searched_user = page.get_by_role("table")
        
    
    def add_employee(self, first_name: str, middle_name: str, last_name: str, employee_id: str):
        self.pim_link.click()
        self.add_employee_button.click()
        self.first_name_input.fill(first_name)
        self.middle_name_input.fill(middle_name)
        self.last_name_input.fill(last_name)
        self.employee_Id_input.fill(employee_id)
        self.save_button.click()
        self.page.wait_for_timeout(3000)
        expect(self.assert_employee).to_contain_text("Kg Uh")
    
    def add_employee_as_user_by_admin(self):
        self.admin_link.click() 
        self.add_user_button.click()
        self.employee_name_input.fill("Kg")
        self.page.wait_for_timeout(3000)
        self.employee_name_option.click()
        self.user_role_dropdown.click()
        self.user_role_option.click()
        self.status_dropdown.click()
        self.status_option.click()
        self.username_input.fill("Kinguh")
        self.password_input.fill("Redeemed123")
        self.confirm_password_input.fill("Redeemed123")
        self.save_user_button.click()   
        self.page.wait_for_timeout(3000)
        expect(self.assert_added_user).to_contain_text("Kinguh")
    
    def confirm_added_user(self):
        self.search_name.fill("Kg")
        self.search_name_option.click()
        self.search_button.click()
        expect(self.assert_searched_user).to_contain_text("Kinguh")
    