import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


count = 10
driver = webdriver.Edge()
driver.get("https://www.facebook.com/pokes")

username_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")

username_input.send_keys("your_email")
password_input.send_keys("your_password")

password_input.send_keys(Keys.ENTER)
while count > 0:
    wait = WebDriverWait(driver, 60)
    poke_back_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="戳回去"]'))
    )

    driver.execute_script("arguments[0].click();", poke_back_element)

    count -= 1

driver.quit()
