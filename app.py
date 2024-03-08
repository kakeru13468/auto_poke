from flask import Flask, request, render_template
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('./login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    count = 1
    driver = webdriver.Edge()
    driver.get("https://www.facebook.com/pokes")

    username_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")

    username_input.send_keys(email)
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)
    while count > 0:
        wait = WebDriverWait(driver, 60)
        poke_back_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="戳回去"]'))
        )

        driver.execute_script("arguments[0].click();", poke_back_element)

        count -= 1

    driver.quit()

    return "登入成功！"


def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    open_browser()
    app.run()