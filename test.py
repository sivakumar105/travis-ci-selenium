# Dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Web elements
username_ele = (By.ID, 'usernameField')
password_ele = (By.ID, 'passwordField')
submit_btn_ele = (By.XPATH, '//button[text()="Login"]')
#skip page
skip_and_continue_ele = (By.XPATH, '//input[@value="Skip and Continue"]')

# driver Initialization
binary_location = r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome(binary_location)
driver.implicitly_wait(20)
# driver.maximize_window()
driver.get('https://login.naukri.com')

# Login to naukri
username = 'sivakumar4b0@gmail.com'
password = 'samantha44'

driver.find_element(*username_ele).send_keys(username, Keys.TAB)
driver.find_element(*password_ele).send_keys(password)
driver.find_element(*submit_btn_ele).click()

try:
    driver.find_element(*skip_and_continue_ele).click()
except Exception as e:
    pass

element_to_hover_over = driver.find_element_by_xpath('//div[@class="mTxt" and contains(text(),"My Naukri")]')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
driver.find_element_by_xpath('//*[@title="Logout"]')
#
# # Now moving to edit profile
driver.find_element_by_xpath('//*[@title="Edit Profile"]').click()

value = 0.5
while value <= 1:
    driver.execute_script("window.scrollTo(0, {}*document.body.scrollHeight);".format(value))
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="attachCV"]'))
        )
        driver.find_element_by_xpath('//input[@id="attachCV"]').send_keys(
            os.path.join(os.getcwd(), "Profile.docx"))
        print 'Done Successfully'
        import time
        time.sleep(10)
        break
    except Exception as e:
        print e, e.message
        value += 0.1
driver.close()


