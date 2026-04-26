## OrangeHRM UI Test Automation Framework

A scalable UI test automation framework built using **Playwright**, **Python**, **Pytest**, and **Page Object Model (POM)** design pattern.
This project automates end-to-end testing of the OrangeHRM demo application and demonstrates best practices for maintainable test automation. 
It supports parallel execution, HTML reporting, and real-time CI feedback.

---

## Tech Stack

* Python 3.x
* Playwright
* Pytest
* Git & GitHub
* Slack API (Notifications)

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
git clone https://github.com/kingsleyuhons/OrangeHRM-Playwright-Python-Pytest.git
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
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest playwright
playwright install
```

---

##  Run Tests Locally

```
pytest -v -n auto --html=report.html --self-contained-html --junitxml=results.xml
```

Run specific test:

```
pytest tests/test_login.py  --html=report.html --self-contained-html --junitxml=results.xml
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
## Example Test 2 (Advanced)

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

# CI/CD with Jenkins

**Pipeline Features**:

* Auto-trigger on GitHub PR merge
* Environment setup (venv + dependencies)
* Parallel test execution
* Report generation
* Slack notifications

---

# GitHub ↔ Jenkins Integration

**Step 1: Install Required Jenkins Plugins**:

* Git Plugin
* Pipeline Plugin
* GitHub Integration Plugin

---
**Step 2: Configure GitHub Webhook**:
1. Go to GitHub repo **→ Settings → Webhooks**
2. Click **Add Webhook**
3. Set
* **Payload URL:** http://<****>/github-webhook/
* **Content type:** application/json
* **Events:** Select Just the push event (or PR events if needed)
---
**Step 3: Configure Jenkins Job**:
* Enable: GitHub hook trigger for GITScm polling
* Branch: */main

---

# Result

Every **pull request merge to main** will automatically:

* Trigger Jenkins build
* Pull latest code
* Run tests
* Send results to Slack

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
* GitHub Actions CI pipeline
* Allure reporting
* Docker support

---

## Kingsley Uhonmhoibhi

QA Automation Engineer
Playwright | Python | Pytest | API Testing | CI/CD

---
-----

