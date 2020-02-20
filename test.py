from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import os
options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument("--no-sandbox")
options.add_argument("window-size=1920,1080")

driver = Chrome(options=options)

print ("Headless Chrome Initialized")

web_link="https://formstone.it/components/dropdown/"
driver.get(web_link)
print (str(web_link)+" opened")
# print(driver.get_window_size())

driver.find_element_by_id("demo_label-dropdown-selected").click()
driver.find_element_by_xpath("(//button[@type='button'])[39]").click()
file_name="docker_screenshot.png"
driver.save_screenshot(file_name)

driver.close()

# Unix
os.popen('cp '+file_name+' /tmp/.')