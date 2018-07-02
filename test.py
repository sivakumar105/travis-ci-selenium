# Dependencies
from selenium import webdriver

binary_location = r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome(binary_location)
driver.implicitly_wait(20)


# Navigate to http://espn.go.com/
driver.get("http://espn.go.com/")


driver.close()

