from selenium.webdriver.common.by import By
class FormPage:
    """
    Этот класс описывает страницу формы анкеты, где можно ввести данные о себе и при нажатии кнопки просмотреть обязательность заполнения каждого поля
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.maximize_window()
    def input_firstname(self, firstname: str):
        """
        Ввести в поле firstname значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(firstname)

    def input_lastname(self, lastname: str):
        """
        Ввести в поле lastname значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(lastname)

    def input_address(self, address: str):
        """
        Ввести в поле address значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def input_email(self, email: str):
        """
        Ввести в поле email значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)

    def input_phone(self, phone: int):
        """
        Ввести в поле phone значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def input_city(self, city: str):
        """
        Ввести в поле city значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def input_country(self, country: str):
        """
        Ввести в поле country значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def input_job(self, job: str):
        """
        Ввести в поле job значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job)

    def input_company(self, company: str):
        """
        Ввести в поле company значение, переданное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit(self):
        """
        Нажать кнопку submit
        """
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        
    def zip_code(self) -> str:
        """
        Вычитать данные элемента zip_code
        """
        zip_code_element = self._driver.find_element(By.CSS_SELECTOR, '#zip-code')
        return zip_code_element
    def first_name(self) -> str:
        """
        Вычитать данные элемента first_name
        """
        first_name_element = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        return first_name_element
    def last_name(self) -> str:
        """
        Вычитать данные элемента last_name
        """
        last_name_element = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        return last_name_element
    def address(self) -> str:
        """
        Вычитать данные элемента address
        """
        address_element = self._driver.find_element(By.CSS_SELECTOR, '#address')
        return address_element
    def email(self) -> str:
        """
        Вычитать данные элемента email
        """
        email_element = self._driver.find_element(By.CSS_SELECTOR, '#e-mail')
        return email_element
    def phone(self) -> str:
        """
        Вычитать данные элемента phone
        """
        phone_element = self._driver.find_element(By.CSS_SELECTOR, '#phone')
        return phone_element
    def city(self) -> str:
        """
        Вычитать данные элемента city
        """
        city_element = self._driver.find_element(By.CSS_SELECTOR, '#city')
        return city_element
    def country(self) -> str:
        """
        Вычитать данные элемента country
        """
        country_element = self._driver.find_element(By.CSS_SELECTOR, '#country')
        return country_element
    def job(self) -> str:
        """
        Вычитать данные элемента job
        """
        job_element = self._driver.find_element(By.CSS_SELECTOR, '#job-position')
        return job_element
    def company(self) -> str:
        """
        Вычитать данные элемента company
        """
        company_element = self._driver.find_element(By.CSS_SELECTOR, '#company')
        return company_element