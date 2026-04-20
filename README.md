## OrangeHRM UI Test Automation Framework

A scalable UI test automation framework built using **Playwright**, **Python**, **Pytest**, and **Page Object Model (POM)** design pattern.
This project automates core workflows of the OrangeHRM demo application and demonstrates best practices for maintainable test automation.

---

## Tech Stack

* Python 3.x
* Playwright
* Pytest
* Page Object Model (POM)
* Git & GitHub

---

## Project Structure

```
Playwright-Projects-orangehrm/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_admin_workflow.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```

---

## Automated Test Scenarios

* Valid login
* Invalid login
* Dashboard validation
* Logout functionality
* Admin user management workflow

---

## Framework Features

* Page Object Model design
* Reusable page methods
* Pytest fixtures
* Clean test separation
* Easy scalability
* CI/CD friendly
* Headed & headless execution support

---

## Installation

### 1. Clone repository

```
git clone https://github.com/<your-username>/orangehrm-playwright-pytest.git
cd Orangehrm-Playwright-Python-Pytest
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate environment:

**Windows**

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install pytest playwright
playwright install
```

---

##  Run Tests

Run all tests:

```
pytest
```

Run in headed mode:

```
pytest --headed
```

Run specific test:

```
pytest tests/test_login.py
```

---

## Example Test 1

```
def test_valid_login(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    dashboard_page = OrangeHRMDashboardPage(page)
    
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    dashboard_page.is_dashboard_visible()
```
## Example Test 2 (Advanced):

```
def test_add_employee_and_create_user(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    admin_page = OrangeHRMAdminPage(page)
   
    login_page.navigate()
    login_page.login("Admin", "admin123")
    admin_page.add_employee("Kg", "E", "Uh", "9909")
    admin_page.add_employee_as_user_by_admin()
    admin_page.confirm_added_user()
```
---

# Design Pattern

This framework uses **Page Object Model (POM)** to:

* Improve maintainability
* Reduce code duplication
* Increase readability
* Enable easy scaling

---

## Future Improvements

* Test data management
* Parallel execution
* GitHub Actions CI pipeline
* Allure reporting
* Docker support

---

## Kingsley Uhonmhoibhi

QA Automation Engineer
Playwright | Python | Pytest | API Testing | CI/CD

---
-----

