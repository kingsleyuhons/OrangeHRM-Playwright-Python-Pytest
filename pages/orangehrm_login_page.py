from playwright.sync_api import Page, expect

class OrangeHRMLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")
        self.empty_field_error_message = page.locator("form")
    
    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        
    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)
        
    def login (self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def click_login(self):
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_url("**/dashboard/index")
        
    def get_error_message (self):
        expect(self.error_message).to_contain_text("Invalid credentials")
        
    def get_empty_field_error_message(self):
        expect(self.empty_field_error_message).to_contain_text("Required")
        
  
        