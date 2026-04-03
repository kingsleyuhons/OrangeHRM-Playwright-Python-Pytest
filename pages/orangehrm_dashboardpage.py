from playwright.sync_api import Page, expect
class OrangeHRMDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_link = page.get_by_role("listitem").filter(has_text="Dashboard")
        self.profile_picture = page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.logout_option = page.get_by_role("menuitem", name="Logout")
        
        
    def is_dashboard_visible(self):
        expect(self.dashboard_link).to_be_visible()
        
    def profile_picture_click(self):
        self.profile_picture.click()
    
    def click_logout(self):
        self.logout_option.click()