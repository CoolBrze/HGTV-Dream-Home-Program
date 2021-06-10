import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


### ENTER YOUR CHROME DRIVER PATH HERE ###
chrome_driver_path = 
driver = webdriver.Chrome(executable_path=chrome_driver_path)


HGTV_URL = 'https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes/'
DISCOVER_URL = 'https://www.discovery.com/sponsored/hgtv-smart-home/'
#### ENTER YOUR LIST OF EMAILS HERE ####
EMAILS = []

for email in EMAILS:
    try:
        driver.get(HGTV_URL)
        time.sleep(2)
        iframe = driver.find_element_by_xpath('/html/body/section/div[3]/div[3]/div/div[2]/div[1]/div/div[3]/div[1]/div/iframe')
        driver.switch_to.frame(iframe)
        time.sleep(1)
        email_input = driver.find_element_by_tag_name('input')
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)

        enter_button = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[2]/div[2]/div/button')
        enter_button.click()
        print("You were successfully entered!")
        driver.quit()

    except selenium.common.exceptions.ElementNotInteractableException:
        print("Already entered today, moving on to next email")

    try:
        driver.get(DISCOVER_URL)
        time.sleep(2)
        iframe = driver.find_element_by_xpath('/html/body/section/div[3]/div[3]/div/div[2]/div[1]/div/div[3]/div[1]/div/iframe')
        driver.switch_to.frame(iframe)
        time.sleep(1)
        email_input = driver.find_element_by_tag_name('input')
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)

        enter_button = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[2]/div[2]/div/button')
        enter_button.click()
        print("You were successfully entered!")
        driver.quit()
    except selenium.common.exceptions.ElementNotInteractableException:
        print("Already entered today, moving on to next email")
