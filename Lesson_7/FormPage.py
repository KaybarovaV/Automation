from selenium.webdriver.common.by import By
class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.maximize_window()
    def input_firstname(self, firstname):
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(firstname)
    def input_lastname(self, lastname):
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(lastname)
    def input_address(self, address):
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
    def input_email(self, email):
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)
    def input_phone(self, phone):
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
    def input_city(self, city):
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
    def input_country(self, country):
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
    def input_job(self, job):
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job)
    def input_company(self, company):
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    def zip_code(self):
        zip_code_element = self._driver.find_element(By.CSS_SELECTOR, '#zip-code')
        return zip_code_element
    def first_name(self):
        first_name_element = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        return first_name_element
    def last_name(self):
        last_name_element = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        return last_name_element
    def address(self):
        address_element = self._driver.find_element(By.CSS_SELECTOR, '#address')
        return address_element
    def email(self):
        email_element = self._driver.find_element(By.CSS_SELECTOR, '#e-mail')
        return email_element
    def phone(self):
        phone_element = self._driver.find_element(By.CSS_SELECTOR, '#phone')
        return phone_element
    def city(self):
        city_element = self._driver.find_element(By.CSS_SELECTOR, '#city')
        return city_element
    def country(self):
        country_element = self._driver.find_element(By.CSS_SELECTOR, '#country')
        return country_element
    def job(self):
        job_element = self._driver.find_element(By.CSS_SELECTOR, '#job-position')
        return job_element
    def company(self):
        company_element = self._driver.find_element(By.CSS_SELECTOR, '#company')
        return company_element