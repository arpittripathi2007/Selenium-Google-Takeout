from selenium import webdriver
from bs4 import BeautifulSoup
import time, requests

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('/home/dell/Documents/Aha-Loans/Practicing/Selenium/IncomeTaxAutoamtion/chromedriver')
driver.set_window_size(1024,600)
driver.maximize_window()

driver.delete_all_cookies()
print("-------------------------------------")
try:
    time.sleep(5)
    print("===============================")
    input_string = "Aggarwal Electrical & Hardware Store"
    # input_string.replace(" ", "-")
    driver.get('https://www.justdial.com/Noida/'+input_string)


    # time.sleep(5)
except:
    print("ERROR OCCURRED")
driver.find_element_by_xpath('// *[ @ id = "tab-5"] / ul / li[1]').click()

