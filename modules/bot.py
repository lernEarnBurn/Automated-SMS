from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

import time




def sendMessage(message, number):

    options = Options()
    #options.add_experimental_option("detach", True)
    #options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)


    load_dotenv()

    driver.get('https://entrancegrp.com/login')
    driver.maximize_window()

    email = driver.find_element(By.XPATH, "//input[@id='inputFieldemail']")
    email.send_keys(os.getenv('entranceEmail'))

    password = driver.find_element(By.XPATH, "//input[@id='inputFieldpassword']")
    password.send_keys(os.getenv('entrancePassword'))

    loginForm = driver.find_element(By.XPATH, "//form[@action='/login']")
    loginForm.submit()

    finish = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-success.ml-2")))
    finish.click()

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
    

    sendBtnSelected = driver.find_element("xpath", "/html/body/main/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[5]/button")
    sendBtn = wait.until(EC.element_to_be_clickable(sendBtnSelected))
    
    sendBtn.click()

    time.sleep(2)
    
    
    
    
'''
for i in range(2):
    sendMessage('', '4692071247')
'''