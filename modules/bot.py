from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from googleSheets import formatNumber

from dotenv import load_dotenv

import time




options = Options()
options.add_argument("--silent")
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

args = ["hide_console", ]


driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe', options=options, service_args=args)
wait = WebDriverWait(driver, 20)


load_dotenv()

def openBrowser():


    driver.get('https://entrancegrp.com/login')
    
    email = driver.find_element(By.XPATH, "//input[@id='inputFieldemail']")
    email.send_keys('email')

    password = driver.find_element(By.XPATH, "//input[@id='inputFieldpassword']")
    password.send_keys('password')

    loginForm = driver.find_element(By.XPATH, "//form[@action='/login']")
    loginForm.submit()

    finish = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-success.ml-2")))
    finish.click()

def sendMessage(message, number):
    messageTab =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".side-menu__item.tra")))
    messageTab.click()

    messageBtn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-small.mr-2.btn-success")))
    messageBtn.click()
    
    numberInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control.numbers-container")))
    numberInput.click()
    numberInput.send_keys(number)

    messageInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control.mb-2")))
    messageInput.click()

    messageInput.send_keys(message)
    messageInput.send_keys(" ")
    messageInput.send_keys(" ")

    sendBtnSelected = driver.find_element("xpath", "/html/body/main/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[5]/button")
    sendBtn = wait.until(EC.element_to_be_clickable(sendBtnSelected))
    
    sendBtn.click()

    time.sleep(2)

    dashboardTab = driver.find_element("xpath", '//*[@id="app"]/div/aside/div[2]/ul/li[1]/button')
    dashboardTab.click()

def closeBrowser():
    driver.quit()
    
    
def getResponseNumbers():
    responseNumbers = []

    messageTab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".side-menu__item.tra")))
    messageTab.click()

    selectContainer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".channel-number")))
    selectContainer.click()

    body = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

    numbers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".channel-number")))
    amountToHave =  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[1]/div[1]/span[1]')))
    
    while len(numbers) != int(amountToHave.text):
        body.send_keys(Keys.ARROW_DOWN)
        numbers = driver.find_elements(By.CSS_SELECTOR, ".channel-number")


    numbers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".channel-number")))
    for number in numbers:
        responseNumbers.append(formatNumber(number.text))
        #responseNumbers.append("")

    print(len(responseNumbers))


    return [number[1:] for number in responseNumbers]