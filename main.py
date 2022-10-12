# Ryan Christopher
# Written 10/12/22
# Created automated test script to simulate 3 test cases
#   1. A Successful Login
#   2. Locking the account with 3 failed attempts
#   3. Successfully resetting the password

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
user = 'jsmith123'      # Username

# Update after resetting password
pwd = 'S3cr3tP@ss2'     # Password

def openWeb():
    # Opens up to selected webpage
    driver.get("http://www.eplanservices.com")

    # Let page open up completely before selecting something
    time.sleep(2)

    # Click sign in button
    driver.find_element(By.XPATH, '/html/body/app-root/div[1]/app-navbar/header/div/div/div[3]/div/a').click()

def loginAttempt(username, password):
    # Write username
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/div[1]/input').send_keys(username)

    # Write password
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/div[2]/input').send_keys(password)

    # Pause to verify
    time.sleep(2)

    # Click login button
    driver.find_element(By.XPATH, '//*[@id="loginButton"]').click()

    # Pause
    time.sleep(2)

def clearLogin():
    # Clear Username and Password
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/div[1]/input').clear()
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/div[2]/input').clear()

def successful_login():
    openWeb()
    loginAttempt(user, pwd)

    # Answer Security Question
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/div[2]/input').send_keys('ePlan')

    # Pause to Verify
    time.sleep(2)

    # Click submit button
    driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()

    # Pause to verify
    time.sleep(5)



def unsuccessful_login():
# Sign out from home page

    # Click Username
    driver.find_element(By.XPATH, '//*[@id="profileName"]').click()
    time.sleep(2)

    # Click Sign Out
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/content/ng-include[1]/div/ng-include[2]/div/div[3]/div[2]/div[2]/ul/li[2]/a').click()
    time.sleep(2)

    # Click No thanks
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div[2]/a[1]').click()
    time.sleep(2)

# Provide 3 failed login attempts
    loginAttempt(user, 'password')
    clearLogin()
    loginAttempt(user, 'password1')
    clearLogin()
    loginAttempt(user, 'password123')
    clearLogin()

    # Provide correct login to show account is truly locked
    loginAttempt(user, pwd)

def reset_account():
    # Click on "having trouble signing in?"
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div[2]/form/a').click()
    time.sleep(2)

    # Click on "Reset my password"
    driver.find_element(By.XPATH, '//*[@id="resetPasswordButton"]').click()
    time.sleep(2)

    # Provide username
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user)
    time.sleep(2)

    # Click Continue
    driver.find_element(By.XPATH, '//*[@id="continueButton"]').click()
    time.sleep(2)

    # Provide security question
    driver.find_element(By.XPATH, '//*[@id="secQuestion"]').send_keys('ePlan')
    time.sleep(2)

    # Click Finish
    driver.find_element(By.XPATH, '//*[@id="finishButton"]').click()

    # Pause and close
    time.sleep(3)
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    successful_login()
    unsuccessful_login()
    reset_account()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
